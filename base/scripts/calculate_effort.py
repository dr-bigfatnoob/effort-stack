#!/usr/bin/python

#
# Returns (prints to STDOUT) the estimated effort for a project
#
# Effort is given for the whole lifespan of the project as well as for semesters
# The effort estimatinos is given for several threshold values t
#
# In the context of the MSR 2014, this script should be launched as follows:
# $ python calculate_effort.py output_authors_ids.csv answers_openstack.csv output_commits.csv
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

import recreate_authors
import answers_openstack
import compare_distributions

authorList = recreate_authors.recreate(sys.argv[1])
authorDict = answers_openstack.survey(sys.argv[2])
activityDict = compare_distributions.activity(sys.argv[3])

semesterList = [-54, -48, -42, -36, -30, -24, -18, -12]

effortList = []

for threshold in range(1,51):
    effortDict = {}
    commits_full = 0
    commits_total = 0
    for author_id in activityDict:
        if author_id in (2, 129, 1209):
            continue
        effortDict[author_id] = []

#        print activityDict[author_id]
        for semester in semesterList:
            commits = 0
            for month in range(semester, semester+6):
                commits += int(activityDict[author_id][month])
#                print month, commits
            if commits >= threshold:
                effortDict[author_id].append(6)
                commits_full += commits
            else:
                effortDict[author_id].append(6.0 * commits/threshold)
            commits_total += commits
#        print effortDict[author_id]
#    print effortDict 
    effortList.append(effortDict)
#    print threshold, commits_total, commits_full, round(commits_full*1.0/commits_total,2)
    print str(round(commits_full*1.0/commits_total,3)) + ',',
print
#print effortList

count = 1
print "# threshold, total_effort, semester1, semester2, semester3, semester4, ..."
for effortDict in effortList:

    effort_total = 0
    for author in effortDict:
        for effort_semester in effortDict[author]:
            effort_total += effort_semester

    effortList = [0] * len(semesterList) 
    for author in effortDict:
        effortList = [x + y for x, y in zip(effortList, effortDict[author])]

    print count, int(round(effort_total)), 
    for sem_effort in effortList:
        print int(round(sem_effort)),
    print
    count+=1
