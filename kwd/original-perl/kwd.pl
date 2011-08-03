#!/usr/bin/perl
# KWD1
# Part of KRU
# Copyright Kwpolska 2010-2011. Licensed under GPLv3.

#KWD1 will be obsolete when KWD2 comes out.

use warnings;
use strict;
use Config::Tiny;
# reading configuration
my $dir = "$ENV{HOME}/.kwd/";
my $config = Config::Tiny->new;
$config = Config::Tiny->read($dir."kwdrc.ini");
my $defcpr = $config->{kwd}->{defcpr};
my $spacer = $config->{kwd}->{spacer};
my $cpname = $config->{kwd}->{cpname};

#hello user, I seem to work fine.

print "KWD v1, a part of KRU, copyright Kwpolska 2010-2011.\n";
print "Licensed under GPLv3.\n\n";

#user input time!

print "1. Main program information\n";
print "1> ";
my $maininfo = <STDIN>;

print "2. Purpose\n";
print "2> ";
my $purpose = <STDIN>;

print "3. Install instructions\n";
print "3> ";
my $instructions = <STDIN>;

print "4. Additional notes -- leave empty if not needed\n";
print "4> ";
my $notesbase = <STDIN>;

print "5. Usage instructions -- leave empty if not needed\n";
print "5> ";
my $usagebase = <STDIN>;

print "6. Copyright note - leave empty for default or type '?' for list\n";
print "6> ";
my $license = <STDIN>;
chomp($license);
if ($license eq '?') {
    print "Avaliable licenses: ";
    my @files = glob($dir.'lic/*');
    foreach my $file (@files) {
        $file =~ s|/.*/lic/||;
        print "$file ";
    }
}

print "7. Save the file as:\n";
print "7> ";
my $location = <STDIN>;

#I love this.  I really do.
chomp($maininfo);
$maininfo =~ s/\\n/\n/g;
chomp($purpose);
$purpose =~ s/\\n/\n/g;
chomp($instructions);
$instructions =~ s/\\n/\n/g;
chomp($location);
chomp($notesbase);
$notesbase =~ s/\\n/\n/g;
chomp($usagebase);
$usagebase =~ s/\\n/\n/g;
chomp($license);
my $notes = '';

#does anyone use it?
if ($notesbase ne "") {
    $notes = "\nNOTES\n$spacer\n$notesbase\n";
}
if ($usagebase ne "") {
    $notes .= "\nUSAGE\n$spacer\n$usagebase\n";
}

#finally, we can open them.
my $baselic;
if ($license eq "") {
    $baselic = $defcpr;
    $license = $dir."lic/".$defcpr;
} else {
    $baselic = $license;
    $license = $dir."lic/".$license;
}
open(my $from, '<', $dir."template") or die "Can't read the template!  $!\n";
open(my $to, '>', $location) or die "Can't create the destination file!  $!\n";
open(my $lic, '<', $license) or die "Can't open the copyright notice!  $!\n";

#reading the copyright notice...
#my @copy = <$lic>;
my $copy = join('', <$lic>);
my $usedata = $config->{usedataincopyright}->{$baselic};
my @lt = localtime(time);
my $year = $lt[5] + 1900; # <3 Y2K
my $copyright;
if ($usedata eq "true") {
    $copyright = sprintf($copy, $year, $cpname);
} else {
    $copyright = $copy;
}
#that's almost it.
print "Writing...";
while(<$from>) {
    $_ =~ s/_KWDPURPOSE_/$purpose/;
    $_ =~ s/_KWDMAININFO_/$maininfo/;
    $_ =~ s/_KWDINSTRUCTIONS_/$instructions/;
    $_ =~ s/_KWDNOTES_/$notes/;
    $_ =~ s/_KWDCOPYRIGHT_/$copyright/;
    print $to $_;
}
# In case you're wondering why aren't they sprintf, I can tell you:
# users don't have to use the exact same order as I do.
print " done.\n";
print "Created file:  ".$location."\n";