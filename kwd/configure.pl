#!/usr/bin/env perl
# KWD
# Part of KRU
# Copyright Kwpolska 2010. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;
my $dir = "$ENV{HOME}/.kwd/";

print "KWD, part of KRU, copyright Kwpolska 2010-2011. Licensed under GPLv3.\n";
print "Configuration\n\n";

print "What is the spacer of NOTES/USAGE? (eg. -----)\n> "
my $spacer = <STDIN>;
print "\nWhat is the default copyright notice?\nDefault ones shipped with KWD: gplv3 bsd\n> ";
my $defcpr = <STDIN>;
print "\nWhat is your name? (required for copyright notices)\n> ";
my $cpname = <STDIN>;

print "\nSaving...";
my $config = Config::Tiny->new;
print " ";
$config->{_}->{defcpr} = $defcpr;
print "d";
$config->{_}->{spacer} = $spacer;
print "o";
$config->{_}->{cpname} = $cpname;
print "n";
$config->write($dir."kwdrc.ini");
print "e\n";
