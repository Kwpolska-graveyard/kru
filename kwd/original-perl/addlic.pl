#!/usr/bin/env perl
# KWD addlic
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;
use File::Basename;
use File::Copy;
my $dir = "$ENV{HOME}/.kwd/";

print "KWD, part of KRU, copyright Kwpolska 2010-2011.  Licensed under GPLv3.\n";
print "Adding a copyright notice\n\n";

print "\nWhere is the notice? (please don't use dashes and semicolons in the filename)\n> ";
my $file = <STDIN>;
print "\nDo you want to use the current year and your name (in that order!) in this copyright notice? [Y/n] ";
my $udic = <STDIN>;

chomp($file);
chomp($udic);
my $udtf = $udic eq 'n' ? 'false' : 'true';
my $bname = fileparse($file, qr/\.[^.]*/);

print "\nSaving...";
copy($file, $dir."licenses/".$bname);
my $config = Config::Tiny->new;
$config = Config::Tiny->read($dir."kwdrc.ini");
$config->{usedataincopyright}->{$bname} = $udtf;
$config->write($dir."kwdrc.ini");
print " done\n";
print "To add another license, run addlic.pl again.\n";
