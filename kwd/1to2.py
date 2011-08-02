#!/usr/bin/env python2
# KWD2 1to2
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

import os
dir = os.path.expanduser("~/.kwd/")

print "KWD2 1to2: version converter\n"
raw_input('Press Enter to convert or ^C to cancel.')

c = open(dir+'template', 'r').read()+'{0}{5}'

c = c.replace('_KWDMAININFO_', '{1}')
c = c.replace('_KWDPURPOSE_', '{2}')
c = c.replace('_KWDINSTRUCTIONS_', '{3}')
c = c.replace('_KWDNOTES_', '{4}')
c = c.replace('_KWDCOPYRIGHT_', '{6}')

open(dir+'template', 'w').write(c)
print "Converting done."
print "Please open the file {0}kwdrc.ini and replace 'spacer' with 'nheadr' \
and 'uheadr'.  nheadr is the notes header and uheadr is the usage header. \n\
Example: uheadr = USAGE:\\n-----"
