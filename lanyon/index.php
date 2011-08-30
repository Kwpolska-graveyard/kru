<?php
//Lanyon
//Copyright Kwpolska 2010.
ob_start();
echo '<h1>Lanyon</h1>';
require_once './config.php';
require_once './init.php';
function umsSearch($uname, $plainPasswd) {
    global $users, $salt;
    $passwd = crypt($plainPasswd, $salt);
    foreach($users as $id => $user) {
        if(strtolower($user['uname']) == strtolower($uname) && $user['passwd'] == $passwd) return $id;
    }
    return false; // the script will return false if no user was found
} //end umsSearch();

if(!isset($_SESSION['uid'])) $_SESSION['uid'] = 0; //anonymous
if($_SESSION['uid'] > 0) {
    echo '<ul>
        <li><a href="./index.php">Home</a></li>
        <li><a href="./add.php">Add</a></li>
        <li><a href="./regenerate.php">Regenerate</a></li>
        <li><a href="./logout.php">Logout</a></li>
        </ul>
        Welcome to Lanyon. Here are all of your posts:
        <ul><form action="del.php" method="POST">';
    $d = dir($jekylldir.'/_posts');
    while (false !== ($entry = $d->read())) {
        if($entry != '.' && $entry != '..') echo "<li><button type=\"submit\" name="delete" value=\'$entry\'>DELETE</button> $entry</li>";
    }
    die '</form></ul>';
}
//Nobody's logged in. Somebody must do so.

//Anybody logged in now?
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    if(($id = umsSearch($_POST['uname'], $_POST['passwd']) !== false) {
            //there is such user.
            $_SESSION['uid'] = $id;
            echo '<ul>
            <li><a href="./index.php">Home</a></li>
            <li><a href="./add.php">Add</a></li>
            <li><a href="./regenerate.php">Regenerate</a></li>
            <li><a href="./logout.php">Logout</a></li>
            </ul>
            <div class=\"info\">Successfully logged in.</div>
            Welcome to Lanyon. Here are all of your posts:
            <ul><form action="del.php" method="POST">';
            $d = dir($jekylldir.'/_posts');
            while (false !== ($entry = $d->read())) {
            if($entry != '.' && $entry != '..') echo "<li><button type=\"submit\" name="delete" value=\'$entry\'>DELETE</button> $entry</li>";
            }
            die '</form></ul>';
            } else {
            echo "<div class=\"error\">Wrong username or password.</div>";
            }
            }
echo '<form method="post" action="?">Please log in.<br>
<input type="text" name="uname"> Username<br>
<input type="password" name="passwd"> Password (case-sensitive!)<br>
<input type="submit" value="Log in">
</form>';
?>

