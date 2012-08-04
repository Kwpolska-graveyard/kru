#!/usr/bin/env python2
# KWD2 1to2
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

import os
kwdir = os.path.expanduser("~/.kwd/")

print "KWD2 1to2: version converter\n"
raw_input('Press Enter to convert or ^C to cancel.')

c = open(kwdir + 'template', 'r').read() + '{0}{5}'

c = c.replace('_KWDMAININFO_', '{1}')
c = c.replace('_KWDPURPOSE_', '{2}')
c = c.replace('_KWDINSTRUCTIONS_', '{3}')
c = c.replace('_KWDNOTES_', '{4}')
c = c.replace('_KWDCOPYRIGHT_', '{6}')

open(kwdir + 'template', 'w').write(c)
print "Converting done."
print "Please open the file {0}kwdrc.ini and replace 'spacer' with 'nheadr' \
and 'uheadr'.  nheadr is the notes header and uheadr is the usage header. \n\
Example: uheadr = USAGE:\\n-----".format(kwdir)
