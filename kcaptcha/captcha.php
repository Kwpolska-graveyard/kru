<?php
# KCAPTCHA
# Copyright (C) 2010-2012, Kwpolska.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

session_start(); # initialize a session
# session protection code
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
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; # Ain't using 0 and O to prevent confusion.
    $captcha            = imagecreatefrompng('./captcha.png');
    $color              = imagecolorallocate($captcha, 255, 255, 255);
    $font               = './DejaVuSansMono.ttf';
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; # this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); # This is idiot-proof.
    imagettftext($captcha, 20, 2, rand(0, 8), 25, $color, $font, $phrase);
    header('Content-Type: image/png');
    imagepng($captcha);
    break;
case 'text':
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; # Ain't using 0 and O to prevent confusion.
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; # this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); # This is idiot-proof.
    echo '<h1>Kw\'s Captcha</h1>'.PHP_EOL.'<strong>Decode the following code using (in Unix) <code>echo \''.base64_encode($phrase).'\' | base64 -d</code></strong>:'.PHP_EOL;
    echo '<code>'.base64_encode($phrase).'</code>';
    break;
case 'figlet':
    require_once 'Text/Figlet.php';
    $chars              = 'ABCDEFGHIJKLMNPQRSTUVWXYZ123456789'; # Ain't using 0 and O to prevent confusion.
    $phrase             = $chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)].$chars[rand(0, strlen($chars)-1)]; # this code is not very good.  Have a suggestion?  Mail me.
    $_SESSION['phrase'] = md5($phrase); # This is idiot-proof.
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
    # We weren't asked to provide the images.  We must provide the phrase.
    $captcha = $_SESSION['phrase'];
    session_destroy(); # and kill the session.
    session_unset();
}
?>
