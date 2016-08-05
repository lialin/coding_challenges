#!/usr/bin/python
import sys
i =list(sys.stdin.readline().strip().split())
n = int(i[0])
m = int(i[1])
a = int(i[2])
row = int(n/a) if (n%a) == 0 else int(n/a)+1
column = int(m/a) if (m%a) == 0 else int(m/a)+1
num = row * column
print(num)