def fact(num):
    """
    Returns the factorial of a given number
    """
    f = 1
    for i in range(2, num+1):
        f = f*i
    return f

def countTrailZeros(num):
    """
    Counts the number of zeros in the factorial of a given number
    """
    f = fact(num)
    temp = f
    count = 0
    while(temp != 0):
        rem = temp%10
        if rem == 0:
            count = count + 1
        else:
            break
        temp = temp//10

    return count

if __name__ == '__main__':
    print(countTrailZeros(int(input())))
