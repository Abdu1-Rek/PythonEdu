from math import *  
for A in range(1,1000):
    N = 283
    i = ceil(log2(A))
    V = ceil(N * i)/8
    V65536 = ((65536 * V)/1024)/1024
    if V65536 > 15:
        print(A)
        break