import math


def count_digits(num):
    """
    function to get number of digits in a number
    """
    return math.floor(math.log(num, 10)+1)


if __name__ == '__main__':
    num = 338959
    print(count_digits(num))
