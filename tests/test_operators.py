from calculate.operators import Operators

def test_should_make_multiple_addition():
    obj=Operators()
    operations="1+2+3+4"
    result=10
    assert obj.addition(operations) == result

def test_should_make_multiple_substraction():
    operations="10-3-2"
    expected_out=Operators().substraction(operations)
    result=5
    assert  expected_out == result


def test_should_make_multiple_multiplication():
    operations="10*10"
    expected_out=Operators().multiplication(operations)
    result=10*10
    assert expected_out==result

def test_should_make_multiple_division():
    operations="100/2/1"
    expected_out= Operators().division(operations)
    result=50
    assert expected_out==result