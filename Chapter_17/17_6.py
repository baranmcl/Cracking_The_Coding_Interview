'''
Given an array of integers, write a method to find indices m and n such that 
if you sorted elements m through n, the entire array would be sorted.
Minimize n - m (that is, find the smallest such sequence). 
EXAMPLE
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9)
'''
arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

def solution(a):
  n = a[0]
  m = a[0]
  for i in range(len(a)):
    if n <= a[i+1]:
      n = a[i]
      print(a[i])
  return a
  
print(solution(arr))
