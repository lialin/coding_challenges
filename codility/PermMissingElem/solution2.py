# Author: lialin
# Email: lianglin@outlook.com
# Date: 2016-04-06
class Solution:
  def solution(self, A):
    n = len(A)
    B = [False] * n
    for val in A:
      if val <=n and val > 0:
	B[val-1] = True
    for i in xrange(n):
      if B[i] == False:
	return i+1
    return n+1
  
