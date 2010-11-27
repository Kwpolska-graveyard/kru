#!/usr/bin/perl
# PKGBUILDer
# Part of KRU
# Copyright Kwpolska 2010. Licensed on GPLv3.
#USAGE: ./build pkg1 [pkg2] [pkg3] (and more)

use warnings;
use strict;
use LWP::Simple;
use Archive::Any;

sub generate {
	my $pkg=shift;
	my $tar=$pkg.".tar.gz";
	my $url="http://aur.archlinux.org/packages/".$pkg."/".$tar;

#let's download the file.
	getstore($url, "./".$tar);

#untar it...
	my $archive = Archive::Any->new("./".$tar);
	$archive->extract;
	system('cd '.$pkg.'; time makepkg -si');
}

my $argc = $#ARGV + 1;
my $i = 0;
if ($argc eq '0') {
print "ERROR: No package specified.
HINT:  ./build.pl pkg [pkg2]\n";
}
while ($i != $argc) {
	my $arg = $ARGV[$i]; #There was no other way.
		generate($arg);
	$i = $i + 1;
}
