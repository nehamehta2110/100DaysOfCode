def fact(number):
    """
    Returns the factorial of a number
    """
    if number==0:
        return 1
    
    return number * fact(number-1)

if __name__ == '__main__':
    print(fact(3))