'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
(e.g.,"waterbottle" is a rotation of "erbottlewat").
'''

def isSubstring(word1, word2):

    return True
    
def isRotation(word1, word2):
    if isSubstring(word1, word2):
        for i in range(len(word1)):
            if word2[len(word2)-i:]+word2[:len(word2)-i] == word1:
                return True
    return False

if __name__ == '__main__':
    print(isRotation("waterbottle", "erbottlewat"))
    print(isRotation("waterbottle", "bottler"))
