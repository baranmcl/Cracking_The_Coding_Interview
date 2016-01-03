''' Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string. '''
#I don't know C or C++ (yet) so here's my solution in Python.
def stringReverse(n):
    return ''.join(str(i) for i in n[-1::-1])
    
if __name__ == '__main__':
    print(stringReverse('backwards!123@$-'))
