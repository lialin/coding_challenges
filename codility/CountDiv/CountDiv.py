# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-09-14
class Solution:
    def solution(self, A, B, K):
        counter = B/K - A/K
        if A % K == 0:
            return counter + 1
        return counter
