#!/usr/bin/perl
# KwDocumentator
# Copyright Kwpolska 2010. Licensed on GPLv2.
use warnings;
print "KwDocumentator\nCopyright Kwpolska 2010. Licensed on GPLv2.\n\n";


print "1. Main program information\ne: Kw's Pastebin. Minimalistic as hell.\n> ";
my $maininfo = <STDIN>;

print "2. Purpose\ne: The pastebin was written originally on request for personal use. Now, the project was published.\n> ";
my $purpose = <STDIN>;

print "3. Install instructions. \ne: Check out the INSTALL file. I promise it wouldn't take long. The project requires PHP 5.1 or newer. PHP 5.0 requires getting PDO.\n> ";
my $instructions = <STDIN>;

print "4. Save the file as:\n> ";
my $location = <STDIN>;
chomp($location);

print "Saving data... ";
open($fh, '>', $location) or die "Wrong chmods to $!";
#you can edit the template here:
print $fh <<THEND;
$maininfo
$purpose
$instructions
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
print "done\a\n";

