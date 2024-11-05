from math import *
for N in range(1, 1000):
    A = 10 + 52 + 980
    i = ceil(log2(A))
    V = ceil((N * i) / 8)
    V385 = (V * 385)/1024
    if V385 < 136:
        print(N)