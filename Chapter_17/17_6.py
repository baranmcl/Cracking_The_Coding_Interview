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
  #scan left to right to find first value out of order
  scanLtoR = 0
  scanLtoRIndex = 0
  for i in a:
    if a[i] < a[i+1]:
      scanLtoR = a[i+1]
      scanLtoRIndex = i+1
    else:
      break
  print(scanLtoR, scanLtoRIndex)
  #scan right to left to find first value out of order
  scanRtoL = 0
  scanRtoLIndex = 0
  #INSERT SCANNING CODE HERE
  #scan through the min and the max indices, and test if values are outside min and max values
  #if outside, expand min and max by one and repeat previous step
  #return min and max indices

print(solution(arr))
