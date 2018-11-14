def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError()
    if n % 15 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return str(n)
