# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, M):
    
    result = 0
    
    m = [0 for _ in range(M)]
    
    for i in range(0, len(A)):
        m[(A[i]) % M] += 1
        
    for i in m:
        if(i > result):
            result = i
    
    return result
