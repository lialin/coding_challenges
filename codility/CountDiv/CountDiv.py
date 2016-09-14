# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-09-14
class Solution:
    def solution(self, A, B, K):
        if A % K == 0:
            return B/K - A/K + 1
        else:
            return B/K - A/K
