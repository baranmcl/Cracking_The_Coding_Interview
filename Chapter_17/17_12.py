'''
Design an algorithm to find all pairs of integers within an array which sum to a specified value.
'''
#if the array is sorted
#binary search for number that adds to array number to get desired sum
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binarySearch(a_list, item):
  first = 0
  last = len(a_list)-1
  found = False
  
  while first <= last and not found:
    midpoint = (first + last)//2
    if a_list[midpoint] == item:
      found = True
    else:
      if item < a_list[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  return found

def pairCount(a_list, desired_total):
  count = 0
  first = 0
  while first < len(a_list):
    target = desired_total - a_list[first]
    if binarySearch(a_list, target):
      count += 1
    first += 1
  return int(count/2)

print(pairCount(a1, 14))

#if the array is unsorted
#sort the array
a2 = [2, 4, 7, 6, 5, 1, 3, 9, 10, 8]

def insertionSort(a_list):
  for index in range(1, len(a_list)):
    currentvalue = a_list[index]
    position = index
    
    while position > 0 and a_list[position-1]>currentvalue:
      a_list[position] = a_list[position-1]
      position = position-1
      
    a_list[position] = currentvalue
  return a_list
  
print(insertionSort(a2))
#do a binary search
print(pairCount(insertionSort(a2), 14))
