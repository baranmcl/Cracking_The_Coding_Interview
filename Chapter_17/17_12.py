'''
Design an algorithm to find all pairs of integers within an array which sum to a specified value.
'''
#if the array is sorted
#binary search for number that adds to array number to get desired sum
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False
  
  while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  return found

def pairCount(alist, desired_total):
  count = 0
  first = 0
  while first < len(alist):
    target = desired_total - alist[first]
    if binarySearch(alist, target):
      count += 1
    first += 1
  return int(count/2)

print(pairCount(a1, 14))

#if the array is unsorted
#sort the array
a2 = [2, 4, 7, 6, 5, 1, 3, 9, 10, 8]


#do a binary search
