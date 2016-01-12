''' Given two strings, write a method to decide if one is a permutation of the other. '''
def permCheck(string1, string2):
    string1Hash = {}
    for i in string1:
        if i not in string1Hash:
            string1Hash[i] = 1
        else:
            string1Hash[i] += 1
    for i in string2:
        if i in string1Hash:
            string1Hash[i] -= 1
        else:
            return False
    for i in string1Hash:
        if string1Hash[i] != 0:
            return False
    return True
    
if __name__ == '__main__':
    print(permCheck('taxis', 'satix'))
    print(permCheck('taxis', 'TAXIS'))
    print(permCheck('TaXis', 'Six'))
