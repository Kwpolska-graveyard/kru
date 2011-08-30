<?php
//Lanyon
//Copyright Kwpolska 2010.
require_once './config.php';
require_once './init.php';
echo '<h1>Lanyon</h1>
<ul>
<li><a href="./index.php">Home</a></li>
<li><a href="./add.php">Add</a></li>
<li><a href="./regenerate.php">Regenerate</a></li>
<li><a href="./logout.php">Logout</a></li>
</ul>';

if(isset($_POST['submit'])) {
    if($_POST['submit'] == "YES") {
        unlink($jekylldir.'/_posts/'.$_POST['delete']) or die("Check your
                chmods.");
        die("<div class=\"info\">The file was successfully deleted.</div>");
    } else {
        die("<div class\"error\">Not deleting the file.</div>");
    }
}
echo 'Are you sure you want to delete the file
<strong>'.$_POST['delete'].'</strong>?
<form action="?" method="POST"><input type="submit" name="submit"
value="YES"> <input type="submit" name="submit" value="NO"> <input
type="hidden" name="delete" value="'.$_POST['delete'].'"></form>';
?>
