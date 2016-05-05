#!/usr/bin/python

#
# Given a CSV with the survey data
# Returns (prints to STDOUT) an anonified CSV of the survey data
#
#

#
# Copyright (C) 2014 GSyC/LibreSoft - Universidad Rey Juan Carlos
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors :
#       Gregorio Robles <grex@gsyc.urjc.es>

import sys

input = open(sys.argv[1], 'r')

while 1:
    line = input.readline()
    if not line:
        break
    elements = line[:-1].split(',')
    print elements[0] + ",,," + ','.join(elements[3:-2])
