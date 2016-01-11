''' Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string. '''
#I don't know C or C++ (yet) so here's my solution in Python.

#def stringReverse(n):
#    return ''.join(str(i) for i in n[-1::-1])

def stringReverse2(n):
    for i in range(int(len(n)/2)):
        n[i], n[len(n)-1-i] = n[len(n)-1-i], n[i]
    return n
    
if __name__ == '__main__':
#    print(stringReverse('backwards!123@$-'))
    print(stringReverse2(["a","v","c","e","d","t"]))
