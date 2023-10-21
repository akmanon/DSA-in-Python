"""
Simple For Loop Program
"""

student_list = []
while True:
    f_name = input("Enter Full name: ")
    student_list.append(f_name)
    print("List of Students are: ")
    for index, stu in enumerate(student_list, start=1): 
        print(f"{index}. {stu}")