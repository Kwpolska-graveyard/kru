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
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $filename = date('Y-m-d-').$_POST['filename'].".markdown";
    file_put_contents($jekylldir.'/_posts/'.$filename, $_POST['cnt']);
    die '<div class=\"info\">Successfully added.</div>';
}
echo '<form method="POST" action="?">
Title in the filename (the date and extension will be added automatically): <input name="filename">
<textarea style="font-family: monospace;" rows="24" cols="80" name="cnt">---
title:
layout: post
---</textarea><br>
<input type="submit" value="Create">
';
?>
