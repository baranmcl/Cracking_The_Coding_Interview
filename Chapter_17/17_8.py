'''
You are given an array of numbers (both positive and negative). Find the continuous sequence with the largest sum.
Return the sum.
EXAMPLE
Input: 2, -8, 3, -2, 4, -10
Output: 5 (i.e., {3, -2, 4})
'''
sample = [2, -8, 3, -2, 4, -10]

def greatestSum(series):
    max_so_far = 0
    max_ending_here = 0
    
    for i in range(0, len(series)):
      max_ending_here = max_ending_here + series[i]
      if max_ending_here < 0:
        max_ending_here = 0
      elif max_ending_here > max_so_far:
        max_so_far = max_ending_here
      
    return max_so_far
    
def greatestSum2(series):
    max_so_far =series[0]
    curr_max = series[0]
    
    for i in range(1,len(series)):
        curr_max = max(series[i], curr_max + series[i])
        max_so_far = max(max_so_far,curr_max)
     
    return max_so_far
    
print(greatestSum(sample), greatestSum2(sample))
