# Author: Liang LIn
# Email: lianglin@outlook.com
# Date: 2017-08-06
from __future__ import division
def solution(A):
    # write your code in Python 2.7
    n = len(A)
    minDiv = 10000
    pointer = 0
    for i in xrange(0, n-2):
        curDiv = min((A[i] + A[i+1]) / 2, (A[i] + A[i+1] + A[i+2]) / 3)
        if(curDiv < minDiv):
            pointer = i
            minDiv = curDiv
    if((A[n-2] + A[n-1])/2 < minDiv):
        pointer = n-2
    return pointer