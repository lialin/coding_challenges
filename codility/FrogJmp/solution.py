class Solution:
    def solution(self, X, Y, D):
        distance = Y - X
        step = distance / D if (distance % D) == 0 else distance / D + 1
        return step