<?php
//KwInstaller
//Part of KRU
//Copyright Kwpolska 2010. Licensed on GPLv2.
if (count($_POST) == 0) {
echo '<form method="POST" action="install.php">
Welcome to the awesome KwInstaller. The only thing I will let you is to edit my config file.<br>
<textarea name="config" cols="80" rows="24">'.file_get_contents('./config.php').'</textarea><br>
<input type="submit" value="ok">
</form>';
} else {
file_put_contents('./config.php', $_POST['config']);
try
	{
		include_once './config.php';
		$pdo = new PDO(DB_DSN, DB_USR, DB_PWD, array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
		$pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$stmt = $pdo -> exec('CREATE TABLE  `'.DB_TNM.'` (
				`code` VARCHAR( 4294967295 ) NOT NULL ,
				`language` VARCHAR( 50 ) NOT NULL ,
				`timestamp` VARCHAR( 50 ) NOT NULL
				) ENGINE = MYISAM'); // edit it with your needs. example from kwpastebin.
		if ($stmt == 0) die('It failed. (code: 0)'); else echo 'Congratulations. (code: 1)';
		unlink('install.php') or die(' failed to remove installer');
	}
catch(PDOException $e)
	{
		echo 'It failed. (code: none), error message:' . $e->getMessage();
	}
}
?>
