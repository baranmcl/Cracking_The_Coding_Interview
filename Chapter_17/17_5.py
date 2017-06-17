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
