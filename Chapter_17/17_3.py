#Write an algorithm which computes the number of trailing zeros in n factorial.
def zeroCountFactorial(n):
  zeroCount = 0
  while n > 0:
    if (n % 5 == 0):
      i = n
      while i > 5: #powers of 5 need to be counted the amount of the exponent.
        if (i / 5 == 5):
          zeroCount += 1
          i = i / 5
      zeroCount += 1
    n -= 1
  return zeroCount
  
def factorial(n):
  ans = 1
  while n > 0:
    ans *= n
    n -= 1
  return ans

def zeroCountText(n):
  text = str(factorial(n))
  count = 0
  for i in text[::-1]:
    if i == "0":
      count += 1
    else:
      break
  return count

print(factorial(25))
print(zeroCountFactorial(25))
print(zeroCountText(25))
