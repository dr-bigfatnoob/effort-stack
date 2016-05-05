#!/usr/bin/python

#
# Returns (prints to STDOUT) R instructions that allow the comparison of the
# population of the project and of the survey population
#
# In the context of the MSR 2014, this script should be launched as follows:
# $ python compare_distributions.py output_authors_ids.csv answers_openstack.csv
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

authorList = recreate_authors.recreate(sys.argv[1])
authorDict = answers_openstack.survey(sys.argv[2])

def activity(filename):
    input = open(filename, "r")

    activityDict = {}
    lineNumber = 1
    while 1:
        line = input.readline()
        if not line:
            break
        activityList = line[:-2].split(',')
        activityDict[authorList[lineNumber-1]] = activityList
        lineNumber +=1
    return activityDict

def list2r(name, inputList):
    returnString = name + " <- c("
    for dev in inputList:
        returnString += str(dev) + ", "
    returnString = returnString[:-2]
    returnString += ")"            
    return returnString


if __name__ == "__main__":
    activityDict = activity("output_commits.csv")

    allList = []
    surveyList = []
    for author_id in activityDict:
        if author_id in (2, 129, 1209):
            continue
        sum_author = 0
        for month in range(-18,-12):
            sum_author += int(activityDict[author_id][month])
        if sum_author > 0:
            allList.append(sum_author)
            if author_id in authorDict:
                surveyList.append(sum_author)


    print list2r("all", allList)
    print list2r("survey", surveyList)
    print 'names(all) <- "all"'
    print 'names(survey) <- "survey"'
    print "summary(all)"
    print "summary(survey)"
    print "wilcox.test(survey,all)"
    print 'png("distribution_boxplot.png")'
    print 'boxplot(survey, all, log="y", main="Distribution of commits",  xlab="Population", ylab="Commits last 6 months (log)", names=c("surveyed active", "all active"))'
    print 'dev.off()'
