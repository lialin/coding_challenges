#!/bin/python

# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-04-07

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    ontime = 0
    for i in a:
        if i <= 0:
            ontime += 1
    if k <= ontime:
        print("NO")
    else:
        print("YES")
