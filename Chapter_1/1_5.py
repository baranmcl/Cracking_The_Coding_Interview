'''
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only upper and lower case letters (a - z).
'''
def compress(string):
    result = ""
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]: 
            count += 1
        else:
            if count > 1:
                result += string[i-count+1] + str(count)
            else:
                result += string[i] + str(count)
            count = 1
    result += string[-1] + str(count)           
    if len(result) >= len(string):
        return string
    return result
    
if __name__ == '__main__':
    print(compress("aabcccccaaa"))
    print(compress("aabbccaa"))
    print(compress("doggy"))
