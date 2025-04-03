import circle
from circle import perimeter
import main
from main import main_function


def test_should_return_perimeter(mocker):
    mocker.patch.object(circle, 'PI', 3.14)
    expected_value = 12.56
    assert perimeter(2) == expected_value




def test_main_function(mocker):
    mocker.patch('main.request', return_value=100)

    expected_value = 100
    assert main_function() == expected_value