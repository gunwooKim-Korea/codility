# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(N):
    
    a = 2863311530 #int(b'10'*8)
    b = 1431655765 #int(b'01'*8)
    
    for i in range(2, int(math.ceil(math.sqrt(N))) + 1):
        
        if(i & a == i) :
            if(((N - i) & a == (N - i)) or (N - i) & b == (N - i)) :
                return i
            pass
        
        elif(i & b == i) :
            if(((N - i) & a == (N - i)) or (N - i) & b == (N - i)) :
                return i
            pass
    return -1
    pass
