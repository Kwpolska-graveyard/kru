#!/usr/bin/perl
# KwDocumentor
# Part of KRU
# Copyright Kwpolska 2010. Licensed on GPLv3.
# Portions copyright Enlik 2010.
use warnings;
use strict;
use Term::ANSIColor qw(:constants);
print "KwDocumentor\nCopyright Kwpolska 2010. Licensed on GPLv3.\n\n";
sub pb {
my $value=shift;
print BOLD, CYAN, '['.$value.'] ', RESET;
}
sub py {
my $value=shift;
print BOLD, YELLOW, '['.$value.'] ', RESET;
}
#template:
#pb("id");
#print "what\n"
#py(">");
#my $value = <STDIN>;
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
#comment the 3 lines below if you don't want to use notes
if ($notesbase ne "") {
$notes = "\nNOTES:\n--------------\n$notesbase\n";
}
#end of commenting area
print "done\n";
py("*");
print "Opening files... ";
open(my $th, '<', './kwdtemplate') or die "Can't read the template!";
open(my $fh, '>', $location) or die "Wrong chmods to $!";
print "done\n";
py("*");
print "Filling... ";
while(<$th>) {
	$_ =~ s/T_PURPOSE/$purpose/;
	$_ =~ s/T_MAININFO/$maininfo/;
	$_ =~ s/T_INSTRUCTIONS/$instructions/;
	$_ =~ s/T_NOTES/$notes/;
	#do you get the template? put below me lines like $_ =~ s/T_STRING_IN_THE_FILE/$variable_there/;
	print "done";
	py("*");
	print "Saving... ";
	print $fh $_; # lub print $fh_dest $_;
}
print "done\n";

