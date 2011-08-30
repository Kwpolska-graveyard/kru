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
</ul>
<pre>';
system($jekyllbin.' '.$jekylldir.' '.$jekyllout);
echo '</pre>';
?>
