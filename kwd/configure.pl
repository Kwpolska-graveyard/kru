#!/usr/bin/env perl
# KWD configurator
# Part of KRU
# Copyright Kwpolska 2010. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;
use File::Copy;

my $dir = "$ENV{HOME}/.kwd/";

print "KWD, part of KRU, copyright Kwpolska 2010-2011.  Licensed under GPLv3.\n";
print "Configuration\n\n";

print "What is the spacer of NOTES/USAGE? (eg. -----)\n> "
my $spacer = <STDIN>;
print "\nWhat is the default copyright notice?\nShipped with KWD: gplv3 mit newbsd freebsd \n> ";
my $defcpr = <STDIN>;
print "\nWhat is your name? (required for copyright notices)\n> ";
my $cpname = <STDIN>;

chomp($spacer):
chomp($defcpr);
chomp($cpname);

print "\nSaving...";
my $config = Config::Tiny->new;
$config->{_}->{defcpr} = $defcpr;
$config->{_}->{spacer} = $spacer;
$config->{_}->{cpname} = $cpname;

$config->{usedataincopyright}->{gplv3}   = "true";
$config->{usedataincopyright}->{mit}     = "true";
$config->{usedataincopyright}->{newbsd}  = "true";
$config->{usedataincopyright}->{freebsd} = "true";

$config->write($dir."kwdrc.ini");
echo " done\n"

echo "Installing copyright notices..."
copy('licenses', $dir);

print " done\n";
print "All done.  To add a new license, run addlic.pl.\n"
