def fact(number):
    """
    Returns the factorial of a number
    """
    f = 1
    for i in range(2, number+1):
        f = f*i
    return f

if __name__ == '__main__':
    print(fact(3))