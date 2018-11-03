import pytest
from fz import fizzbuzz

def test_fizzbuzz_takes_number_returns_str():
    result = fizzbuzz(1)
    assert isinstance(result, str)

@pytest.mark.parametrize(('number', 'expected'),[(1,'1'),
                                                (2, '2'),
                                                (4,'4'),
                                                (7,'7'),
                                                (8,'8')])
def test_regular_returns_numbers(number, expected):
    result = fizzbuzz(number)
    assert result == expected

@pytest.mark.parametrize('number', [3,6,9,12,18, 303, 909, 2727])
def test_3_returns_fizz(number):
    result = fizzbuzz(number)
    assert result == 'fizz'

@pytest.mark.parametrize('number', [5,10,20,25,35,1505])
def test_5_returns_buzz(number):
    result = fizzbuzz(number)
    assert result == 'buzz'

@pytest.mark.parametrize('number', [15,30,45,60,300,3000])
def test_15_returns_buzz(number):
    result = fizzbuzz(number)
    assert result == 'fizzbuzz'

def test_cannot_fizzbuzz_strs():
    with pytest.raises(TypeError):
        fizzbuzz("nope")

def test_cannot_fizzbuzz_anything():
    with pytest.raises(TypeError):
        fizzbuzz(None)

def test_cannot_fizzbuzz_float():
    with pytest.raises(TypeError):
        fizzbuzz(5.5)

# regresne testy
#@pytest.mark.xfail()
def test_xxx():
    assert True #False
