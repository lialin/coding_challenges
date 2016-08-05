#!/bin/python

# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-04-13

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    r = 0
    for i in xrange(n+1):
        if (n-i) % 3 == 0 and i % 5 == 0:
            r = '5' * (n-i) + '3' * i
            break
    if r == 0:
        print('-1')
    else:
        print(r)  
