

n  = 9320
rem = 0
div = n
m = 0
while n >= 1:
    rem = n%10
    print(rem)
    if(rem >= 0 and div%rem == 0):
        m = m+1
    n = n//10
    
print(m)