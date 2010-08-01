<?php
//KwPortal
//Copyright Kwpolska 2009-2010. Licensed on GPLv2.
session_start();
include_once './test.php';
include_once './config.php';
if (count($_POST) == 0) {
$content = '<form method="post" action="add2.php"><input name="title"><br>
<textarea cols="80" rows="43" name="content"></textarea><br>
<input name="send" value="Submit [title|content]" type="submit"></form>';
} else {
	try
	{
		$pdo = new PDO(DB_DSN, DB_USR, DB_PWD, array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
		$pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	
		$stmt = $pdo -> prepare('INSERT INTO `'.DB_TNM.'` (`title`, `content`, `date`) VALUES(
			:title,
			:content,
			:date)');	// 1
		
		$stmt -> bindValue(':title', $_POST['title'], PDO::PARAM_STR);
		$stmt -> bindValue(':date', time(), PDO::PARAM_STR);
		$stmt -> bindValue(':content', $_POST['content'], PDO::PARAM_STR);
		
		$ilosc = $stmt -> execute();
	
		if($ilosc = 1)
		{
			$content = 'Roger that.';
		}
		else
		{
			$content = 'wut?';
		}
	}
	catch(PDOException $e)
	{
		echo 'ERROR: ' . $e->getMessage();
	}
}
$title = 'Add';
smartya();
?>
