<?php
//Lanyon
//Copyright Kwpolska 2010.
require_once './config.php';
require_once './init.php';
session_start();
session_destroy();
session_unset();
echo "See you again!";
?>
