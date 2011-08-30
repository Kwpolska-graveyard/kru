<?php
//Lanyon
//Copyright Kwpolska 2010.

/// JEKYLL SETTINGS ///
$jekyllbin = '/var/lib/gems/1.8/bin/jekyll'; // your jekyll executable
$jekylldir = '/home/Kwpolska/jekyll'; // your jekyll dir
$jekyllout = '/home/Kwpolska/www'; // your generated HTML for Jekyll

/// USER SETTINGS ///
$saltbase = 'kwportalsawesome'; //up to 16 characters, longer ones will be trimmed
$users = array(1 =>
        array('uname' => 'USERNAME', 'passwd' => 'A SHA512 PASSWORD'),
        );

/// DYNAMIC SETTINGS ///
$salt = '$6$rounds=5000$'.$saltbase.'$';
?>
