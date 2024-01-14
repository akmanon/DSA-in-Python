def mul(*args):
    z = 1
    print(len(args))
    for num in args:
        z *= num
    return z

