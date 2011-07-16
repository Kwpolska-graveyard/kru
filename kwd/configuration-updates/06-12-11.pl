#!/usr/bin/perl
# KWD configuration update
# 06/12/11
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

use warnings;
use strict;
use Config::Tiny;
use File::Copy;

my $dir = "$ENV{HOME}/.kwd/";

#updatedata
my $newDate     = '06/12/11';
my $oldDate     = '05/14/11';
my $userInput   = 0;
my $changeLog   = "Entries are now in [kwd] section";
sub gatherInput {
    #nothing to do
}
sub configUpdate {
    open my $cfg, '<', $dir.'kwdrc.ini.bak' or die "Can't read the config!  $!\n";
    open my $out, '>', $dir.'kwdrc.ini' or die "Can't create the new file!  $!\n";
    print {$out} '[kwd]'."\n";
    while(<$cfg>) {
        print {$out} $_;
    }
}

#welcome the user
print "KWD configuration update\n$newDate\n\n";

#changelog
print "Changes since last update ($oldDate):\n";
print "$changeLog\n\n";

#user input (eg. new options)
if ($userInput == 0) {
    print "No user input required.\n";
} else {
    print "User input required.\n";
    gatherInput();
}
print "\n";

#confirmation
print "Continue? (Y/n) ";
my $confirmation = <STDIN>;
chomp $confirmation;
print "\n";
if ($confirmation =~ /no?/i) {
    print "Update aborted by user.  No changes were made to your file.\n";
    exit 0
} else {
    #actual update
    print "Creating a backup (at ".$dir."kwdrc.ini.bak)...";
    copy($dir.'kwdrc.ini', $dir.'kwdrc.ini.bak') or die "Backup failed!  $!\n";
    print " done.\nExecuting the update...";
    configUpdate();
    print " done.\n\nAll done.  Search for any other updates.\n";
}
