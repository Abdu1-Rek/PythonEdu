from math import *
for N in range(1,1000):
    A = 10 + 52 + 5000
    i = ceil(log2(A))
    V = ceil((N * i) / 8)
    V949 = ( 949 * V ) / 1024
    if V949 > 727:
        print(N)
        break