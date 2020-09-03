from random import randrange, getrandbits


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


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


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if x < 0:
        x = x + m0

    return x


def generate_public_key():
    return generate_prime_number(length=800), generate_prime_number(length=800), 65537


def generate_private_key(p, q, e):
    return mod_inverse(e, (p - 1) * (q - 1))


def get_encoded_message():
    message = input("Enter message: ")
    encoded_message = ""

    for i in range(len(message)):
        current_char = str(ord(message[i]))
        if len(current_char) < 3:
            current_char = '0' * (3 - len(current_char)) + current_char
        encoded_message += current_char

    return encoded_message, message


def convert_encoded_to_normal(encoded):
    normal_message = ""
    while encoded > 0:
        char_encoding = encoded % 1000
        normal_message = chr(char_encoding) + normal_message
        encoded //= 1000
    return normal_message


def encrypt(m, p, q, e):
    return pow(m, e, p * q)


def decrypt(encoded, private, n):
    return pow(encoded, private, n)


if __name__ == '__main__':
    encoded_message, message = get_encoded_message()
    p, q, e = generate_public_key()
    print("N=" + str(p * q))
    private_key = generate_private_key(p, q, e)
    encrypted = encrypt(int(encoded_message), p, q, e)
    decrypted = decrypt(encrypted, private_key, p * q)
    print("Original Message: " + str(encoded_message))
    print("Encrypted Message: " + str(encrypted))
    print("Decrypted Message: " + convert_encoded_to_normal(decrypted))


