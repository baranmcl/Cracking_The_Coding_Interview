'''
Design a method to find the frequency of occurences of any given word in a book.
'''
bookText = ("You see how many people are selling it, and crucially, you see how many people are buying it for what price.")

def wordCount(word, text):
  wordArray = text.strip().split(" ")
  count = 0
  for i in wordArray:
    if word == i:
      count += 1
  return count
  
print(wordCount("you", bookText))
