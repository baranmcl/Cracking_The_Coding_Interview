''' Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? '''
def stringCheck(n):
    characters = []
    for i in n:
        if i not in characters: characters.append(i)
        else: return False
    return True
  
if __name__ == '__main__':
    print(stringCheck('the quick brown fox'))
    print(stringCheck('abcdefghijklmnop'))
