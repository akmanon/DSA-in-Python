"""
Simple Script to Sum all interger
"""


def sumup(num=1):
    res = 0
    for i in range(1, num + 1):
        res = res + i
    return res

num = int(input("Enter Number to get sum of all integer: "))

if num > 0:
    result = sumup(num)
    print(f"Sum of all interger is {result}")
else:
    print("Invalid Number") 

    print()