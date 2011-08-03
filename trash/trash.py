#!/usr/bin/env python2.6
# trash
# Part of KRU
# Copyright Kwpolska 2011.  Licensed under GPLv3.
import shutil
import os
import subprocess
import datetime
import sys
import argparse


ktdirectory = os.path.expanduser("~/.local/share/Trash")

def createTrash():
    if os.path.exists(ktdirectory) == False:
        mkdir(ktdirectory)
    os.mkdir(ktdirectory+'/files')
    os.mkdir(ktdirectory+'/info')
    infofile = '[Cached]\nSize=0'
    open(ktdirectory+'/metadata', "w").write(infofile)

def emptyTrash():
    """Empties the trash."""
    shutil.rmtree(ktdirectory+'/files')
    shutil.rmtree(ktdirectory+'/info')
    createTrash()
    sys.stderr.write("emptied the trash")

def listFiles():
    """Lists the trash contents (using /bin/ls)."""
    subprocess.call('/bin/ls --color=auto '+ktdirectory+'/files', shell=True)

def moveToTrash(filename):
    """Moves specified files to trash."""
    os.rename(filename, ktdirectory+'/info/'+os.path.basename(filename))
    infofile = '[Trash \
    Info]\nPath={0}\nDeletionDate={1}'.format(realpath(filename),
        datetime.datetime.now().strftime('%Y-%m-%dT%H:%m:%S'))
    open(ktdirectory+'/files/'+os.path.basename(filename)+'.trashinfo',
            "w").write(infofile)

def moveToTrashVerbose(filename):
    """Verbosely moves specified files to trash."""
    moveToTrash(filename)
    sys.stderr.write("trashed `{0}'".format(filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple trash script. \
                                     Part of KRU, copyright Kwpolska 2011, \
                                     licensed under GPLv3.")
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

    if os.path.exists(ktdirectory) == False:
        print "`{0}' does not exist, creating...".format(ktdirectory)
        createTrash()

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