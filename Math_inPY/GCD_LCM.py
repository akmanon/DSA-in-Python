def gcd(a, b):
    while b:
        a, b = b, a%b
        print(f"A: {a} \nB: {b} \n---")
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

print(lcm(12, 21))