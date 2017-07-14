#Write a method which finds the maximum of two numbers. You should not use if-else or any other comparison operator. 
import math

def maximum(a, b):
  return (math.sqrt((a*a) + (b*b) - (2*a*b)) + a + b) / 2
  
print(maximum(-10, 4))
