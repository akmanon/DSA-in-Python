"""
In python there in no native switch statement
But we can acheive if-elif-else to acheive the same
"""


day_no = input("Enter Number between 1 - 7 ")

def switch(day):
    if day == "6":
        print("It's Weekend")
    elif day =="7":
        print("It's Weekend")
    elif int(day) >= 1 and int(day) <= 5:
        print("Not a weekend")
    else:
        print("Invalid Input")


switch(day_no)