#!/usr/bin/perl
# KwDocumentator
# Part of KRU
# Copyright Kwpolska 2010. Licensed on GPLv2.
use warnings;
use Term::ANSIColor;
print "KwDocumentator\nCopyright Kwpolska 2010. Licensed on GPLv2.\n\n";
sub printblue {
my $value=shift;
print color 'blue';
print '['.$value.'] ';
print color 'reset';
}
printblue("1");
print "Main program information\n";
my $maininfo = <STDIN>;

print "Purpose\n";
my $purpose = <STDIN>;

print "Install instructions\n";
my $instructions = <STDIN>;

print "Additional notes - leave empty if needed\n";
my $notesbase = <STDIN>;

print "Save the file as:\n";
my $location = <STDIN>;

print "Preparing... ";
chomp($maininfo);
chomp($purpose);
chomp($instructions);
chomp($location);
chomp($notesbase);
my $notes = '';
if ($notesbase ne "") {
$notes = "\nNOTES:\n--------------\n$notesbase\n";
}
print "done\n";
print "Saving data... ";
open($fh, '>', $location) or die "Wrong chmods to $!";
#you can edit the template here:
print $fh <<THEND;
$maininfo
--------------

PURPOSE:
--------------
$purpose

INSTALLATION:
--------------
$instructions
$notes
COPYRIGHT:
--------------
Copyright (C) 2010 Kwpolska.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
THEND
close $fh;
print "done\n";

