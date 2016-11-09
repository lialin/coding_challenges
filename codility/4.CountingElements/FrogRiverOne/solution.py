# Author: Liang Lin
# Email: lin.lag@gmail.com
# Date: 2016-03-24
class Solution:
  def solution(self, X, A):
    B = [False] * X
    counter = 0
    for i, val in enumerate(A):
      if val <= X:
          B[val-1] = True
          while B[counter]:
	    counter += 1
	    if counter >= X:
	      return i
    return -1