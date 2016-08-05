# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-03-27
class Solution:
  def solution(self, N, A):
    #max counter
    mc = 0
    lmc = 0
    '''
    :type B: List[int]
    :rtype: int
    '''
    B = [0] * N
    for i, val in enumerate(A):
      if val == N + 1:
        lmc = mc
      else:
        B[val-1] = max(lmc+1, B[val-1]+1)
        mc = max(mc, B[val-1])

    for i, val in enumerate(B):
      B[i] = max(lmc, val)
    return B
sol = Solution()
print(sol.solution(3,[2,1,1,2,3,4,1,2,3,2,2]))
      