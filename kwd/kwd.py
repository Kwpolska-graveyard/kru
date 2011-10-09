#!/usr/bin/env python2
# KWD v2.0.1
# Part of KRU
# Copyright Kwpolska 2011. Licensed under GPLv3.
"""
A readme generator.  Originally written in Perl.
"""
import ConfigParser
import os
import datetime
import sys
import gettext

T = gettext.translation('kwd', '/usr/share/locale', fallback='en')
_ = T.gettext

class Cstorage:
    """A place for storing config data."""
    def __init__(self):
        """C init."""
        self.kwdir    = os.path.expanduser("~/.kwd/")
        self.config   = None
        self.nheadr   = ''
        self.uheadr   = ''
        self.defcpr   = ''
        self.cpname   = ''

    def populate(self, configfile = ''):
        """Populate C with data."""
        if configfile == '':
            configfile = self.kwdir+'kwdrc.ini'

        self.config = ConfigParser.ConfigParser()
        self.config.read(configfile)
        self.nheadr   = self.config.get('kwd', 'nheadr')
        self.uheadr   = self.config.get('kwd', 'uheadr')
        self.defcpr   = self.config.get('kwd', 'defcpr')
        self.cpname   = self.config.get('kwd', 'cpname')

    def reload(self, kwdir = "~/.kwd/"):
        """Reloads C."""
        self.__init__()
        self.kwdir    = os.path.expanduser(kwdir)
        self.populate()

class Istorage:
    """A place for storing input data."""
    def __init__(self):
        """I init."""
        self.header   = ''
        self.purpose  = ''
        self.install  = ''
        self.notesb   = ''
        self.usageb   = ''
        self.licname  = ''
        self.fname    = ''

    def ask_for_input(self, number, text, hint=''):
        """A function for inputting data."""
        #if hint != '':
        print '{0}. {1} ({2})'.format(number, text, hint)
        #else:
        #    print '{0}. {1} '.format(number, text)
        return raw_input('>  ')

    def populate(self):
        """Populate I with data."""
        self.header   = self.ask_for_input(1, _('Header'), _('usually \
the name'))
        self.purpose  = self.ask_for_input(2, _('Purpose of the app'),
                       _('you can use \\n'))
        self.install  = self.ask_for_input(3, _('selfnstall instructions'),
                       _('you can use \\n'))
        self.notesb   = self.ask_for_input(4, _('Notes'), _('leave empty if \
not needed'))
        self.usageb   = self.ask_for_input(5, _('Usage'), _('leave empty if \
not needed'))
        self.licname  = self.ask_for_input(6, _('License'), _('leave empty \
for default)\n(possible: {0}').format(', '.join(os.listdir(C.kwdir+'lic'))))
        self.fname    = self.ask_for_input(7, _('Filename'), _('the file \
in which the README will be written, use - for stdout'))


class Gstorage:
    """A place for storing generated data."""
    def __init__(self):
        """G init."""
        self.noteuse  = ''
        self.template = ''
        self.lictext  = ''
        self.licfinal = ''
        self.final    = ''
    def generatefb(self):
        """Generates file-based data."""
        self.template = open(C.kwdir+'template', 'r').read()
        self.lictext  = open(C.kwdir+'lic/'+I.licname, 'r').read()

    def generatelic(self):
        """Generates licfinal."""
        self.licfinal = self.lictext % (datetime.date.today().year, C.cpname)

    def generatefinal(self):
        """Generates final."""
        #{0} and {5} are cheats.  And licname is backwards-compatible.
        self.final    = self.template.format('', I.header, I.purpose,
                                             I.install, self.noteuse, '',
                                             self.licfinal)

#Yes, I know, it sounds like the Hungarian notation, but that's the best way.
C = Cstorage()
I = Istorage()
G = Gstorage()

C.populate()


print _("""KWD v2.0.1, part of KRU, copyright Kwpolska 2010-2011.
Licensed under GPLv3.""")

I.populate()

G.noteuse = ''
if I.notesb != '':
    G.noteuse = G.noteuse+C.nheadr+'\n'+I.notesb+'\n'
if I.usageb != '':
    G.noteuse = G.noteuse+C.uheadr+'\n'+I.usageb+'\n'
I.purpose = I.purpose.replace('\\n', '\n')
I.install = I.install.replace('\\n', '\n')
G.noteuse = G.noteuse.replace('\\n', '\n')

if I.licname == '':
    I.licname = C.defcpr

G.generatefb()
G.generatelic()

G.generatefinal()

if I.fname == '-':
    I.fname = sys.stdout

open(I.fname, 'w').write(G.final)

#The code got a little bit longer, because it's a bit more complex.
