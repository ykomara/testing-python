import  unittest
from calculate.operators import Operators
class TestOperator(unittest.TestCase):
    def test_should_make_multiple_addition(self):
        operations="1+2+3"
        expected_out= Operators().addition(operations)
        result=6
        self.assertEqual(expected_out,result, msg="test daddition")

    def test_should_make_multiple_substraction(self):
        operations="100-50-2"
        result=48
        expected_out=Operators().substraction(operations)
        self.assertEqual(expected_out, result)

    def test_should_make_multiple_multiplication(self):
        operations="10*10"
        result=100
        expected_out=Operators().multiplication(operations)
        self.assertEqual(expected_out, result)

    def test_should_make_multiple_division(self):
        operations="100/2"
        result=50
        expected_out=Operators().division(operations)
        self.assertEqual(expected_out, result)



