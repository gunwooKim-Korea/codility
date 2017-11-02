# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import datetime

def solution(S):
    S = S.split('\n')
    
    S = sorted(S, key=lambda item: item[1])
    # print S        
    for item in S:
        tmp = item.split(', ')
        
        tmp = sorted(tmp, key=lambda tmp:tmp[2], reverse=True)
        print tmp
        
        pass
    
    # print S
    pass
