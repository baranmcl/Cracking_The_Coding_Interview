''' 
Write a method to replace all spaces in a string with '%20'. You may assume that the string has
sufficient space at the end of the string to hold the additionanl characters, and that you are given
"true" length of the string. (Note: if implementing in Java, please use a character array so taht you 
can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
'''
def spaceReplace(string, length):
    return string[:length].replace(" ","%20")
    
if __name__ == '__main__':
    print(spaceReplace("Mr John Smith    ", 13))
