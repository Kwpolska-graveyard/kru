#!/usr/bin/env perl
# KPG configurator
# Part of KRU
# Copyright Kwpolska 2010. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;

my $dir = "$ENV{HOME}/.kpg/";

print "KPG, part of KRU, copyright Kwpolska 2010-2011.  Licensed under GPLv3.\n";
print "Configuration\n\n";

print "Where is the template file?\n> ";
my $templt = <STDIN>;
print "\nWhere is Markdown.pl?\n> ";
my $mdpath = <STDIN>;

chomp($templt);
chomp($mdpath);

print "\nSaving...";
my $config = Config::Tiny->new;
$config->{_}->{templt} = $templt;
$config->{_}->{mdpath} = $mdpath;
$config->write($dir."kpgrc.ini");
print " done\n";
