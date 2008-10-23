#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2008 Philippe Pinard"
__license__ = ""
__reference__ = "Altmann (1986) Rotation, Quaternions and Double Groups"

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

def numberOfTriplets(n):
  s = [0]
  
  for i in range(0, n-1):
    s.append(s[-1] + i)
    
  return sum(s)

def findTriplets(n):
  triplets = []
  
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if j > i and (k > j and k > i):
          triplets.append((i,j,k))
  
  return triplets

if __name__ == '__main__':
  print numberOfTriplets(7)
  print len(findTriplets(7))
  print findTriplets(7)