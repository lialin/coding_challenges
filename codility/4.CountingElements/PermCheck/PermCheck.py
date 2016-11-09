# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-03-26
class Solution:
  def solution(self, A):
    n = len(A)
    B = [False] * n
    for i in range(n):
        if A[i] > n or A[i] < 1 or B[A[i]-1]:
            return 0
        else:
            B[A[i]-1] = True
    return 1
