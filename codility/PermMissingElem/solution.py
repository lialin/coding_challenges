class Solution:
    def solution(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        actualSum = sum(i for i in A)
        expectedSum = sum(range(1,n+2))
        return expectedSum - actualSum