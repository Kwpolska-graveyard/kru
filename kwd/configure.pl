#!/usr/bin/env perl
# KWD configurator
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;
use File::Copy;

my $dir = "$ENV{HOME}/.kwd/";

print "KWD, part of KRU, copyright Kwpolska 2010-2011.  Licensed under GPLv3.\n";
print "Configuration\n\n";

print "What is the spacer of NOTES/USAGE? (eg. -----)\n> ";
my $spacer = <STDIN>;
print "\nWhat is the default copyright notice?\nShipped with KWD: freebsd gplv3 mit newbsd \n> ";
my $defcpr = <STDIN>;
print "\nWhat is your name? (required for copyright notices)\n> ";
my $cpname = <STDIN>;

chomp($spacer);
chomp($defcpr);
chomp($cpname);

print "\nSaving...";
my $config = Config::Tiny->new;
$config->{kwd}->{defcpr} = $defcpr;
$config->{kwd}->{spacer} = $spacer;
$config->{kwd}->{cpname} = $cpname;

$config->{usedataincopyright}->{freebsd} = "true";
$config->{usedataincopyright}->{gplv3}   = "true";
$config->{usedataincopyright}->{mit}     = "true";
$config->{usedataincopyright}->{newbsd}  = "true";

$config->write($dir."kwdrc.ini");
print " done\n";

print "Installing copyright notices...";
copy('lic', $dir);
unlink($dir.'lic/CONTENTS');
print " done\n";
print "All done.  To add a new license, run addlic.pl.\n";
