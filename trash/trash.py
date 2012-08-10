#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# trash
# Part of KRU
# Copyright (C) 2011-2012, Kwpolska.
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

import shutil
import os
import subprocess
import datetime
import sys
import argparse
ktdirectory = os.path.expanduser("~/.local/share/Trash")


def createTrash():
    if not os.path.exists(ktdirectory):
        os.mkdir(ktdirectory)
    os.mkdir(ktdirectory + '/files')
    os.mkdir(ktdirectory + '/info')
    infofile = '[Cached]\nSize=0'
    open(ktdirectory + '/metadata', "w").write(infofile)


def emptyTrash(verbose):
    """Empties the trash."""
    shutil.rmtree(ktdirectory + '/files')
    shutil.rmtree(ktdirectory + '/info')
    createTrash()
    if verbose:
        sys.stderr.write("emptied the trash\n")


def listFiles():
    """Lists the trash contents (using /bin/ls)."""
    subprocess.call('/bin/ls -CF --color=auto ' + ktdirectory + '/files',
                    shell=True)


def moveToTrash(filename, verbose):
    """Moves specified files to trash."""
    os.rename(filename, ktdirectory + '/files/' + os.path.basename(filename))
    infofile = '[Trash \
Info]\nPath={0}\nDeletionDate={1}'.format(os.path.realpath(filename),
                                          (datetime.datetime.now()
                                          .strftime('%Y-%m-%dT%H:%m:%S')))
    open(ktdirectory + '/info/' + os.path.basename(filename) + '.trashinfo',
         'w').write(infofile)

    if verbose:
        sys.stderr.write("trashed ‘{0}’\n".format(filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple trash script. \
                                     Part of KRU, copyright Kwpolska 2011.")
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

    if not os.path.exists(ktdirectory):
        sys.stderr.write("“{0}” does not exist, creating...".format(
            ktdirectory))
        createTrash()

    if args.flist:
        listFiles()
        shallExit = True

    if args.empty:
        emptyTrash(args.verbose)
        shallExit = True

    if shallExit:
        exit()

    # Did not exit?  Let's trash the files, shan’t we?
    for filename in args.files:
        moveToTrash(filename, args.verbose)
