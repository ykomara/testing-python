from calculate.operators import Operators

def test_should_make_multiple_addition():
    obj=Operators()
    operations="1+2+3+4"
    result=10
    assert obj.addition(operations) == result