#!/usr/bin/env python2
# KWD2 configure
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

import ConfigParser
import sys
import os
import shutil
dir = os.path.expanduser("~/.kwd/")

print "KWD v2, part of KRU, copyright Kwpolska 2010-2011. \
Licensed under GPLv3."
print "KWD configure: configuration file creator\n"

print "NOTES/USAGE spacer (eg. -----)"
spacer = raw_input('> ')

print "\nDefault copyright notice:\n  Already available: \
freebsd gplv3 mit newbsd"
defcpr = raw_input('> ')

print "\nName (required for copyright notices):"
cpname = raw_input('> ')

print "\n"

config = ConfigParser.ConfigParser()

config.add_section('kwd')
config.set('kwd', 'spacer', spacer)
config.set('kwd', 'defcpr', defcpr)
config.set('kwd', 'cpname', cpname)

config.add_section('usedataincopyright')
config.set('usedataincopyright', 'freebsd', 'true')
config.set('usedataincopyright', 'gplv3', 'true')
config.set('usedataincopyright', 'mit', 'true')
config.set('usedataincopyright', 'newbsd', 'true')
if os.path.exists(dir) == False:
    os.mkdir(dir)
    shutil.copytree(os.getcwd()+'/lic', dir+'licenses')
    shutil.copy(template, dir)
config.write(open(dir+'kwdrc.ini', 'w'))
