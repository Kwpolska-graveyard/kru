#!/usr/bin/env python2
# KWD2 v1-to-v2
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.

import os
dir = os.path.expanduser("~/.kwd/")

print "KWD2 v1tov2: version converter\n"
raw_input('Press Enter to convert or ^C to cancel.')

fhandle = open(dir+'template', 'r+')
c = fhandle.read()+'{0}{5}'

c = c.replace('_KWDMAININFO_', '{1}')
c = c.replace('_KWDPURPOSE_', '{2}')
c = c.replace('_KWDINSTRUCTIONS_', '{3}')
c = c.replace('_KWDNOTES_', '{4}')
c = c.replace('_KWDCOPYRIGHT_', '{5}')

fhandle.write(c)
print "Done."
