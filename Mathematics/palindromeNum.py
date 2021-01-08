def is_palindrome(num):
    """
    Check if a given number is a palindrome number
    """
    temp = num
    rev = 0
    while(temp!=0):
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp//10
    return rev==num

if __name__ == "__main__":
    print(is_palindrome(5735))
