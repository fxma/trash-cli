#!/usr/bin/python
# trash-empty: remove file from trashcans
#
# Copyright (C) 2008 Einar Orn Olason
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from trashcli.trash import *

def main(argv=None) :
    """
    Empty the trash. If a command line parameter is given we delete only files
    older than that parameter (integer, days).
    """
    # original author: Einar Orn Olason
    # modified by Andrea Francia
    import os, datetime, sys

    trashcan = GlobalTrashCan()

    days=0
    usage="usage: "+sys.argv[0]+" [days]"

    if len(sys.argv) > 2 :
        print usage
        sys.exit()
    elif len(sys.argv) > 1 :
        try :
            days=int(sys.argv[1])
        except :
            print usage
            sys.exit()

    for trashedfile in trashcan.trashed_files() :
        delta=datetime.datetime.now()-trashedfile.deletion_date
        if delta.days >= days :
            trashedfile.purge()

# eof