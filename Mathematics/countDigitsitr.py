def count_digits(num):
    """
    function to get number of digits in a number
    """
    temp = num
    count = 0
    while(temp != 0):
        temp = temp//10
        count += 1
    return count


if __name__ == '__main__':
    num = 338959
    print(count_digits(num))
