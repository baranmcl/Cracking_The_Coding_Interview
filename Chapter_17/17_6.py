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
  scan_L_to_R = 0
  scan_L_to_R_Index = 0
  for i in range(len(a)):
    if a[i] > a[i+1]:
      scan_L_to_R = a[i]
      scan_L_to_R_Index = i
      break
  if (scan_L_to_R_Index == len(a)):
    print("the array is sorted")
    return
  print(scan_L_to_R, scan_L_to_R_Index)
  #scan right to left to find first value out of order
  scan_R_to_L = 0
  scan_R_to_L_Index = 0
  for i in reversed(range(len(a))):
    if a[i] < a[i-1]:
      scan_R_to_L = a[i]
      scan_R_to_L_Index = i
      break
  print(scan_R_to_L, scan_R_to_L_Index)
  #scan through the min and the max indices, and test if values are outside min and max values
  left_arr_max = a[scan_L_to_R_Index]
  right_arr_min = a[scan_R_to_L_Index]
  #if outside, expand min and max by one and repeat previous step
  while max(a[:scan_R_to_L_Index]) > right_arr_min:
    scan_R_to_L_Index -= 1
  while min(a[scan_L_to_R_Index:]) < left_arr_max:
    scan_L_to_R_Index += 1
  #return min and max indices
  return scan_R_to_L_Index, scan_L_to_R_Index
print(solution(arr))
