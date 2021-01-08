def find_gcd(number1, number2):
    """
    Find the GCD of two numbers
    """
    temp = min(number1, number2)
    while(temp>0):
        if number1%temp==0 and number2%temp==0:
            break
        temp = temp-1
    return temp

if __name__ == '__main__':
    print(find_gcd(10,15))
