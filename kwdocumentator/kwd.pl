#!/usr/bin/perl
# KwDocumentator
# Part of KRU
# Copyright Kwpolska 2010. Licensed on GPLv2.
# Portions copyright Enlik 2010.
use warnings;
use strict;
use Term::ANSIColor qw(:constants);
print "KwDocumentator\nCopyright Kwpolska 2010. Licensed on GPLv2.\n\n";
sub pb {
my $value=shift;
print BOLD, CYAN, '['.$value.'] ', RESET;
}
sub py {
my $value=shift;
print BOLD, YELLOW, '['.$value.'] ', RESET;
}
pb("1");
print "Main program information\n";
py(">");
my $maininfo = <STDIN>;
print "\n";
pb("2");
print "Purpose\n";
py(">");
my $purpose = <STDIN>;
print "\n";
pb("3");
print "Install instructions\n";
py(">");
my $instructions = <STDIN>;
print "\n";
pb("4");
print "Additional notes - leave empty if needed\n";
py(">");
my $notesbase = <STDIN>;
print "\n";
pb("5");
print "Save the file as:\n";
py(">");
my $location = <STDIN>;
print "\n";
py("*");
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
py("*");
print "Saving data... ";
open(TH, '<', './kwdtemplate') or die "Can't read the template!";
open(FH, '>', $location) or die "Wrong chmods to $!";
while(<TH>) {
	$_ =~ s/T_PURPOSE/$purpose/;
	$_ =~ s/T_MAININFO/$maininfo/;
	$_ =~ s/T_INSTRUCTIONS/$instructions/;
	$_ =~ s/T_NOTES/$notes/;
}
close FH;
close TH;
print "done\n";

