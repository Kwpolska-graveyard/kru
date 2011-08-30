<?php
//sha512sum
//By Kwpolska. On PD.
require_once './config.php';
//$saltbase = 'jekyllforrubyftw'; //up to 16 characters, longer ones will be trimmed
//$salt = '$6$rounds=5000$'.$saltbase.'$';
if($_SERVER['REQUEST_METHOD'] == 'POST') echo crypt($_POST['passwd'], $salt).'<br>';
echo '<form method="post" action="?"><input type="password" name="passwd"> <input type="submit" value="Generate"></form>';
?>
