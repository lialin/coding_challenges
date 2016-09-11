# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-04-01
class Solution:
    def solution(self, A):
        n = len(A)
        counter = 0
        eastcar = 0
        threshold = 1000000000
        for i in range(n):
            if A[i] == 0:
                eastcar += 1
            else:
                counter += eastcar
                if counter > threshold:
                     return -1
        return counter

sol = Solution()
print(sol.solution([0,1,0,1,1,0,1]))
