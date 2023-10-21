#String 

f_name = input("Enter your first name \n")
l_name = input("Enter your last name \n")

f_char = f_name[0]
l_char = l_name[-1]

full_name = f_name.capitalize() + " " + l_name.capitalize() + "!"


l_full_name = len(full_name)

prompt = f"Your name is {full_name} and code is {f_char.lower() +  l_char.lower()}"

print(prompt)