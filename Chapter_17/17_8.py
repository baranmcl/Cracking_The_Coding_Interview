'''
You are given an array of numbers (both positive and negative). Find the continuous sequence with the largest sum.
Return the sum.
EXAMPLE
Input: 2, -8, 3, -2, 4, -10
Output: 5 (i.e., {3, -2, 4})
'''
Input = [2, -8, 3, -2, 4, -10]

def greatestSum(series):
    answer = 0
    for i in range(0,len(series)):
        total = 0
        for j in range(i+1):
            total += series[j]
        print(str(total) + '!')
        if total > answer:
            answer = total
    return answer
    
print(greatestSum(Input))
