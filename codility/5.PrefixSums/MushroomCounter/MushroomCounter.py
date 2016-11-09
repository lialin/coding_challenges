class Solution:
  def solution(self, A, k, m):
    n = len(A)
    result = 0
    pref = self.prefix_sums(A)
    # starts from 0 to k moving forwards to count m steps
    for p in xrange(min(k,m)+1):
      left_pos = k - p
      # 2*p count the picker moves forward and backward at the same spot
      right_pos = min(n-1, max(k, k+m-2*p))
      result = max(result, self.count_total(pref, left_pos, right_pos))
    # starts from k to n-1 moving backwards to count m steps 
    for p in xrange(min(m+1, n-k)):
      right_pos = k + p
      left_pos = max(0, min(k, k - (m - 2*p)))
      result = max(result, self.count_total(pref, left_pos, right_pos))
    return result
  
  def prefix_sums(self, A):
    n = len(A)
    P = [0] * (n+1)
    for k in xrange(1, n+1):
      P[k] = P[k-1] + A[k-1]
    return P
  
  def count_total(self, P, x, y):
    return P[y+1] - P[x]
  
sol = Solution()
sol.solution([1,8,2,4,5,6,7,1], 3, 5)