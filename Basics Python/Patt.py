import math
n = 3
m = n*2

for i in range(1, n+1):
    for j in range(1, m+1):
        if i >= j and i <= n: 
            print(j, end=" ")
        elif i > m - j:
            print(m-j+1, end=" ")
        else:
            print(" ", end=" ")
    print()