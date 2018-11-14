def fizzbuzz(n):
    '''
    Returns the result of the game. If number is not divisible by 3 or 5, 
    returns provided number. If number is divisible by 3, returns 'fizz',
    if number is divisible by 5, returns 'buzz'. If number is divisible by 3
    and 5, returns 'fizzbuzz'.
    
    Parameters
    ----------
    n: <int>
        Any number.
        
    Returns
    -------
    <str>
        The result of the game.
    '''
    if not isinstance(n, int):
        raise TypeError()
    if n % 15 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return str(n)
