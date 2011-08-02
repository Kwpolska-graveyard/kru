#!/usr/bin/env python2
# KWD2 addlic
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

#If ran without arguments ([--nodata] FILE), asks for input
#on stdin.

import ConfigParser
import sys
import os
import shutil
import argparse
dir = os.path.expanduser("~/.kwd/")
parser = argparse.ArgumentParser(description="KWD2 addlic")
parser.add_argument('--nodata', action='store_false', default=True,
                    dest='data', help="don't use year and date")
parser.add_argument('file', metavar="FILE", action='store',
                    nargs='?', default=False, help="packages to build")
args = parser.parse_args()
print "KWD v2, part of KRU, copyright Kwpolska 2010-2011. \
Licensed under GPLv3."
print "KWD addlic: copyright notice adder\n"

if args.file != False:
    cnf = args.file
    if args.data == True:
        bnd = 'true'
    else:
        bnd = 'false'
else:
    print "File (no semicolons and dashes, shall have no extension):"
    cnf = raw_input('> ')
    und = raw_input('\nUse year and date in notice? [Y/n] ')
    if und[0] == 'n' or und[0] == 'N':
        bnd = 'false'
    else:
        bnd = 'true'

bnf = os.path.basename(cnf)
shutil.copy(cnf, dir+'lic/'+cnf)
config = ConfigParser.ConfigParser()
config.read(dir+'kwdrc.ini')
config.set('usedataincopyright', bnf, bnd)
config.write(open(dir+'kwdrc.ini', 'w'))
print "\nDone, restart to add another one (if needed)"
