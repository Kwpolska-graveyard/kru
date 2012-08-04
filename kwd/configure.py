#!/usr/bin/env python2
# KWD2 configure
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

import ConfigParser
import sys
import os
import shutil
kwdir = os.path.expanduser("~/.config/kwpolska/kwd/")

print "KWD v2, part of KRU, copyright Kwpolska 2010-2011. \
Licensed under GPLv3."
print "KWD configure: configuration file creator\n"

print "Notes header (eg. NOTES:\\n------):"
nheadr = raw_input('> ')

print "Usage header (eg. USAGE:\\n------):"
uheadr = raw_input('> ')

print "\nDefault copyright notice:\n  Already available: \
freebsd gplv3 lgplv3 mit newbsd"
defcpr = raw_input('> ')

print "\nName (required for copyright notices):"
cpname = raw_input('> ')

print "\n"

config = ConfigParser.ConfigParser()

config.add_section('kwd')
config.set('kwd', 'nheadr', nheadr)
config.set('kwd', 'uheadr', uheadr)
config.set('kwd', 'defcpr', defcpr)
config.set('kwd', 'cpname', cpname)

config.add_section('usedataincopyright')
config.set('usedataincopyright', 'freebsd', 'true')
config.set('usedataincopyright', 'gplv3', 'true')
config.set('usedataincopyright', 'mit', 'true')
config.set('usedataincopyright', 'newbsd', 'true')
if not os.path.exists(kwdir):
    os.mkdir(kwdir)
    shutil.copytree(os.getcwd() + '/lic', kwdir + 'licenses')
    shutil.copy(template, kwdir)
config.write(open(kwdir + 'kwdrc.ini', 'w'))
