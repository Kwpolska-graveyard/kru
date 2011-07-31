#!/usr/bin/perl
# PKGBUILDer/build.pl
# Part of KRU
# Copyright Kwpolska 2010-2011. Licensed under GPLv3.
#USAGE: ./build packages

use warnings;
use strict;
use LWP::Simple;
use Archive::Any;
use Term::ANSIColor qw(:constants);

$SIG{'INT' } = 'freset';  $SIG{'QUIT'} = 'freset';
$SIG{'HUP' } = 'freset';  $SIG{'TRAP'} = 'freset';
$SIG{'ABRT'} = 'freset';  $SIG{'STOP'} = 'freset';

sub info {
    print BOLD, GREEN, "==> ", RESET, BOLD, shift."\n", RESET;
}

sub freset {
    print RESET, BOLD, "Okay!\nExiting right now.\n", RESET;
    exit(1);
}

sub help {
    print BOLD, "PKGBUILDer/build.pl", RESET;
    print "Copyright Kwpolska 2010-2011. Licensed under GPLv3.";
    print "Usage: ./build.pl [PACKAGE]...";
#    print "Usage: ./build.pl [-dur] [--download] [--get-unpack] [--root] [PACKAGE]...
#-d, --download      Downloads the package
#-u, --get-unpack    Downloads the package and unpacks it
#-r, --root          Allows working as root (--asroot)";
}

sub kdownload {
    my $pkg=shift;
    my $tar=$pkg.".tar.gz";
    my $url="http://aur.archlinux.org/packages/".$pkg."/".$tar;
    info("Downloading the tarball...");
    getstore($url, "./".$tar);
}

sub kunpack {
    my $pkg=shift;
    my $tar=$pkg.".tar.gz";
    info("Extracting the tarball...");
    my $archive = Archive::Any->new("./".$tar);
    $archive->extract;
}

sub kpackage {
    my $pkg=shift;
    info("Building package ".$pkg."...");

    #let's download the file.
    kdownload($pkg);

    #untar it.
    kunpack($pkg);

    #build it.
    system('cd '.$pkg.'; time makepkg -si');
    info("Package ".$pkg." was successfully bulit.");
}

my $argc = $#ARGV + 1;
my $i = 0;
if ($argc eq '0') {
    print "ERROR: No package specified.";
    help();
}

while ($i != $argc) {
    my $arg = $ARGV[$i]; #There was no other way.
    kpackage($arg);
    $i = $i + 1;
}
