'''
The Game of Master Mind is played as follows:
The computer has four slots, and each slot will contain a ball that is Red (R), yellow (Y), green (G) or blue (B). 
For example, the computer might have RGGB (slot #1 is red, slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB. 
When you guess the correct color for the correct lsot, you get a "hit". if you guess a color that exists but is in the wrong slot, you get a "pseudo-hit". 
Note that a slot that is a hit can never count as a pseudo-hit.
For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo-hit.
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits.
'''
solution = 'RGBY'
guess = input('Enter a guess: ')

def calcPseudoHits(solution, guess, hits):
  #Get counts of correct colors
  solutionDict = {"R":0, "G":0, "B":0, "Y":0}
  guessDict = {"R":0, "G":0, "B":0, "Y":0}
  for i in solution:
    solutionDict[i] += 1
  for i in guess:
    guessDict[i] += 1
  #Find possible hits and subtract actual hits
  pseudoHits = 0
  for i in solutionDict:
    if solutionDict[i] == guessDict[i]:
      pseudoHits += solutionDict[i]
  if pseudoHits - hits < 0:
    return 0
  return pseudoHits - hits

def mastermind(solution, guess):
  hits = 0
  pseudoHits = 0
  for i in range(4):
    if solution[i] == guess[i]:
      hits += 1
  pseudoHits = calcPseudoHits(solution, guess, hits)
  print("Hits: " + str(hits))
  print("Pseudo-Hits: " + str(pseudoHits))
  if solution == guess:
    return "You Win!"
  return "Try Again!"

print(mastermind(solution, guess))
