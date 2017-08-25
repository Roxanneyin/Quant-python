def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p*p < n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_palindrom(n):
    n = str(n)
    if n[::-1] == n:
        return True
    else:
        return False
