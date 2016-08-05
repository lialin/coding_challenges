# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-03-27
'''
class MissingInterger:
  def solution(self, A):
    n = len(A)
    if n == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    for i in sorted(A):
        while A[i] > 0 and A[i] <= n and A[i] != i+1 and A[A[i]-1] != A[i]:
                self.swap(i, A)

    for i in range(n):
        if A[i] != i+1:
            return i+1

  def swap(self, i, A):
    temp = A[i]
    index = A[i]-1
    A[i] = A[index]
    A[index] = temp
'''    
class MissingInterger:
  def solution(self, A):
      n = len(A)
      B = [False] * n
      for val in A:
          if val > 0 and val <= n:
            B[val-1] = True
      for i in range(n):
          if B[i] == False:
              return i+1
      return n+1
      

  
mi = MissingInterger()
print(mi.solution([1]))