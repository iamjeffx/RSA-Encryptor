from random import randrange


def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # Find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # Fo k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


if __name__ == '__main__':
    message = input("Enter message: ")
    encoded_message = ""

    for i in range(len(message)):
        current_char = str(ord(message[i]))
        if len(current_char) < 3:
            current_char = '0' * (3 - len(current_char)) + current_char
        encoded_message += current_char

    print(encoded_message)
    print(is_prime(int(encoded_message)))

