'''
Implement a method rand7() given rand5(). That is, given a method that generates a random number between 0 and 4 (inclusive) 
write a method that generates a random number between 0 and 6 (inclusive).
'''

def rand7():
  matrix = [[0,1,2,3,4], [5,6,0,1,2], [3,4,5,6,0],[1,2,3,4,5],[6,7,7,7,7]]
  answer = 7
  while answer == 7:
    i = rand5()
    j = rand5()
    answer = matrix[i][j]
  return answer
