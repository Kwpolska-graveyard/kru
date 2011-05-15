#!/usr/bin/env python2.6
# trash.py
# Part of KRU
# Copyright Kwpolska 2011.  Licensed under GPLv3.
from shutil import *
from os import *
from os.path import *
from argparse import *
from shlex import *
from subprocess import *
from datetime import date, time, datetime
ktdirectory = expanduser("~/.local/share/Trash")
def emptyTrash():
    """Empties the trash."""
    print ":: Emptying the trash"
    rmtree(ktdirectory+'/files')
    mkdir(ktdirectory+'/files')
    rmtree(ktdirectory+'/info')
    mkdir(ktdirectory+'/info')
    open(ktdirectory+'/metadata', 'w').write('[Cached]\nSize=0')
    print "[DONE]"

def listFiles():
    """Lists the trash contents (using /bin/ls)."""
    call('/bin/ls --color=auto '+ktdirectory, shell=True)

def moveToTrash(filename):
    """Moves specified files to trash."""
    rename(filename, ktdirectory+'/files/'+basename(filename))
    infofile = '[Trash \
    Info]\nPath={0}\nDeletionDate={1}'.format(realpath(filename),
        datetime.now().strftime('%Y-%m-%dT%H:%m:%S'))
    open(ktdirectory+'/metadata/'+basename(filename)+'.trashinfo',
        "w").write(infofile)

def moveToTrashVerbose(filename):
   """Verbosely moves specified files to trash."""
    moveToTrash(filename)
    print "trashed `{0}'".format(filename)


if __name__ == '__main__':
    parser = ArgumentParser(description="A simple trash script.  Part of KRU,\
                            copyright Kwpolska 2011, licensed under GPLv3.")
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help="print more info")
    parser.add_argument('-e', '--empty', action='store_true', default=False,
                        dest='empty', help="empty the trash and exit")
    parser.add_argument('-l', '--list', action='store_true', default=False,
                        dest='flist', help="list the files in trash and exit")
    parser.add_argument('files', metavar="FILE", action='store', nargs='*',
                        help="files to remove")
    args = parser.parse_args()

    shallExit = False

    if args.flist == True:
        listFiles()
        shallExit = True

    if args.empty == True:
        emptyTrash()
        shallExit = True

    if shallExit == True:
        exit()

    # Did not exit?  Let's trash the files, shalln't we?
    for filename in args.files:
        if args.verbose == True:
            moveToTrashVerbose(filename)
        else:
            moveToTrash(filename)
