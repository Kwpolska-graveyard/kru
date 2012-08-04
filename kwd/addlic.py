#!/usr/bin/env python2
# KWD2 addlic
# Part of KRU
# Copyright (C) 2010-2012, Kwpolska.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#If ran without arguments ([--nodata] FILE), asks for input
#on stdin.

import ConfigParser
import sys
import os
import shutil
import argparse
kwdir = os.path.expanduser("~/.kwd/")
parser = argparse.ArgumentParser(description="KWD2 addlic")
parser.add_argument('--nodata', action='store_false', default=True,
                    dest='data', help="don't use year and date")
parser.add_argument('file', metavar="FILE", action='store',
                    nargs='?', default=False, help="packages to build")
args = parser.parse_args()
print "KWD v2, part of KRU, copyright Kwpolska 2010-2011. \
Licensed under GPLv3."
print "KWD addlic: copyright notice adder\n"

if args.file:
    cnf = args.file
    if args.data:
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
shutil.copy(cnf, kwdir + 'lic/' + cnf)
config = ConfigParser.ConfigParser()
config.read(kwdir + 'kwdrc.ini')
config.set('usedataincopyright', bnf, bnd)
config.write(open(kwdir + 'kwdrc.ini', 'w'))
print "\nDone, restart to add another one (if needed)"
