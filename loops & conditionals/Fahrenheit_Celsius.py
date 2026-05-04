import math

S = int(input())
E = int(input())
W = int(input())

for F in range(S, E + 1, W):
    C = (F - 32) * 5 / 9
    
    if C >= 0:
        C = math.floor(C)
    else:
        C = math.ceil(C)
    
    print(F, "\t", C)
