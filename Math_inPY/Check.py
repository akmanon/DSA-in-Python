def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        print(i, number)
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Test the is_prime function
number = 13  # Replace with the number you want to check

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


for i in range(2, int(number**0.5) + 1 ):
    print(i)