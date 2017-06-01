#Write a function to swap a number in-place (That is, without temporary variables).
a = 9
b = 5

def switchVariables(x, y):
  x = y - x
  y = y - x
  x = y + x
  print(x, y)

print(a, b)
switchVariables(a, b)

def binarySwitch(x, y):
  x = y ^ x
  y = x ^ y
  x = y ^ x
  print(x, y)
  
binarySwitch(a, b)
