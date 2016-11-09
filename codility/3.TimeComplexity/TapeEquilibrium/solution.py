class Solution:
  def solution(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    result = 100000
    n = len(A)
    psum = 0
    #sum all the elements
    asum = sum(A[i] for i in range(0, n))
    
    for i in range(n-1):
      psum += A[i]
      asum -= A[i]
      result = min(result, abs(asum-psum))
    return result