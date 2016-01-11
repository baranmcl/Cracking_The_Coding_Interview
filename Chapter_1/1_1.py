''' Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? '''

#ask interviewer if string is ASCII or Unicode.

#def stringCheck(n):
#    characters = []
#    for i in n:
#        if i not in characters: characters.append(i)
#        else: return False
#    return True

def bubbleSort(n):
    for passnum in range(len(n)-1,0,-1):
        for i in range(passnum):
            if n[i]>n[i+1]:
                n[i+1], n[i] = n[i], n[i+1]

def stringCheck2(n):
    if len(n) > 128: return False
    sortedString = bubbleSort(n)
    for letter in range(len(sortedString)):
        if sortedString[letter] == sortedString[letter+1]:
            return False
    return True

if __name__ == '__main__':
    print(stringCheck2('the quick brown fox'))
    print(stringCheck2('abcdefghijklmnop'))
