"""
Let Check if a Person Adult or not, 
"""

age = input("What is ypur Age")

if not (int(age) > 0 and int(age) < 18 ):
    print("You are an Adult")
else:
    print("Not an Adult")