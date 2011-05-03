<?php
/* Kw's CAPTCHA
 * Copyright Kwpolska 2011. Licensed under GPLv3.
 */
session_start(); //initialize a session
// session protection code
if (!isset($_SESSION['init'])) {
    session_regenerate_id();
    $_SESSION['init'] = true;
    $_SESSION['ip'] = $_SERVER['REMOTE_ADDR'];
}

if($_SESSION['ip'] != $_SERVER['REMOTE_ADDR']) {
    session_destroy();
    session_start();
    session_regenerate_id();
    $_SESSION['init'] = true;
    $_SESSION['ip'] = $_SERVER['REMOTE_ADDR'];
}
switch($_GET['action']) {
case 'img':
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; //Ain't using 0 and O to prevent confusion.
    $captcha            = imagecreatefrompng('./captcha.png');
    $color              = imagecolorallocate($captcha, 255, 255, 255);
    $font               = './DejaVuSansMono.ttf';
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; //this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); //This is idiot-proof.
    imagettftext($captcha, 20, 2, rand(0, 8), 25, $color, $font, $phrase);
    header('Content-Type: image/png');
    imagepng($captcha);
    break;
case 'text':
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; //Ain't using 0 and O to prevent confusion.
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; //this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); //This is idiot-proof.
    echo '<h1>Kw\'s Captcha</h1>'.PHP_EOL.'<strong>Decode the following code using (in Unix) <code>echo \''.base64_encode($phrase).'\' | base64 -d</code></strong>:'.PHP_EOL;
    echo '<code>'.base64_encode($phrase).'</code>';
    break;
case 'figlet':
    require_once 'Text/Figlet.php';
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; //Ain't using 0 and O to prevent confusion.
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; //this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); //This is idiot-proof.
    echo "Please write the following characters to the text field. <pre>";

    $figlet = new Text_Figlet();
    $error  = $figlet->LoadFont('slant.flf');
    if (PEAR::isError($error)) {
        echo 'Error: ' . $error->getMessage() . "\n";
    } else {
        echo $figlet->LineEcho($phrase) . "\n";
    }
    echo "</pre>"
    break;
default:
    // We weren't asked to provide the images.  We must provide the phrase.
    $captcha = $_SESSION['phrase'];
    session_destroy(); // and kill the session.
    session_unset();
}
?>
