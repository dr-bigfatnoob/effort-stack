#!/usr/bin/python

#
# Returns (prints to STDOUT) following values for several threshold t:
#   * [tp, fm, tn, fp]
#   * precision 
#   * recall
#   * fmeasure
#   * accuracy,
#   * goodness
#
# In the context of the MSR 2014, this script should be launched as follows:
# $ python precision_recall_semester.py output_authors_ids.csv answers_openstack.csv outoput_commits.csv
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

thresholdList = []

for threshold in range(0, 50):
#    print threshold
    tp, fn, tn, fp = (0, 0, 0, 0)
    for author_id in activityDict:
        if author_id in authorDict:
            if authorDict[author_id][-1] == 0: # no commits!
                continue
            commitment = authorDict[author_id][0][0]
#            print author_id, commitment,
            activity = 0
            for month in range(-18,-12):
                activity += int(activityDict[author_id][month])
#            print activity,

            if (int(activity) > threshold and commitment == 'f'):
                tp += 1
#                print 'tp',
            elif int(activity) <= threshold and commitment != 'f':
                tn += 1
#                print 'tn',
            elif commitment == 'f':
                fn += 1
#                print 'fn',
            else:
                fp += 1
#                print 'fp',
#            print
    thresholdList.append([tp, fn, tn, fp])

i = 0
print "# threshold, [tp, fm, tn, fp], precision, recall, fmeasure, accuracy, goodness"
for threshold in thresholdList:
    print i+1, threshold,
    tp = threshold[0]
    fn = threshold[1]
    tn = threshold[2]
    fp = threshold[3]
    precision = round(tp*1.0/(tp+threshold[-1]),3)
    recall = round(tp*1.0/(tp+fn),3)
    fmeasure = round(2 * precision * recall / (precision + recall),3)
    accuracy = round((tp+tn)*1.0/(tp+fn+tn+fp),3)
    goodness = 1-round(abs((tp + fp)- (tp + fn))*1.0/(tp + fn + fp),3)

    print precision, recall, fmeasure, accuracy, goodness
    i+=1

