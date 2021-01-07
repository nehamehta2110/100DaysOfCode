def count_digits(num):
    """
    function to get number of digits in a number
    """
    if num == 0:
        return 0
    return 1 + count_digits(num//10)


if __name__ == '__main__':
    num = 338959
    print(count_digits(num))
