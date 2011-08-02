#!/usr/bin/env python2
# KWD v2
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.
"""
A readme generator.  Originally written in Perl.
"""
import ConfigParser
import os
import datetime

dir = os.path.expanduser("~/.kwd/")
config = ConfigParser.ConfigParser()
config.read(dir+'kwdrc.ini')
nheadr=config.get('kwd', 'nheadr')
uheadr=config.get('kwd', 'uheadr')
defcpr=config.get('kwd', 'defcpr')
cpname=config.get('kwd', 'cpname')

def askForInput(number, text, hint=''):
    if hint != '':
        print '{0}. {1} ({2})'.format(number, text, hint)
    else:
        print '{0}. {1} '.format(number, text)
    return raw_input('>  ')

print "KWD v2, part of KRU, copyright Kwpolska 2010-2011. \n\
Licensed under GPLv3."

header  = askForInput(1, 'Header', 'usually the name')
purpose = askForInput(2, 'Purpose of the app', 'you can use \\n')
install = askForInput(3, 'Install instructions', 'you can use \\n')
notesb  = askForInput(4, 'Notes', 'leave empty if not needed')
usageb  = askForInput(5, 'Usage', 'leave empty if not needed')
license = askForInput(6, 'License', 'leave empty for default)\n\
(possible: {0}'.format(os.listdir(dir+'lic')))
fname  = askForInput(7, 'Filename')

noteuse = ''
if notesb != '':
    noteuse = noteuse+nheadr+'\n'+notesb+'\n'
if usageb != '':
    noteuse = noteuse+uheadr+'\n'+usageb+'\n'
purpose = purpose.replace('\\n', '\n')
install = install.replace('\\n', '\n')
noteuse = noteuse.replace('\\n', '\n')

#We'd be on line 86 here in v1.  Or ~60 if I'd implement askForInput().

if license == '':
    license = defcpr

template = open(dir+'template', 'r').read()
lictext  = open(dir+'lic/'+license, 'r').read()
licfinal = lictext % (datetime.date.today().year, cpname)
#{0} is a cheat.  And licfinal is backwards-compatible.
final    = template.format('', header, purpose, install, noteuse, '', license)
open(fname, 'w').write(final)

#125 lines in 60.  <3.
