x = -187
y = x
if x > -10 and x < 10 :
    print(x)
    exit()
if x < 0:
    x = x * (-1)
rev = x % 10
x = x//10
while x > 0:
    rev = rev*10 + x%10
    x = x//10
    print(rev)
if y < 0 :
    print(rev * (-1))