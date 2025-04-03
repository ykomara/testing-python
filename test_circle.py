import circle
from circle import perimeter
import main
from main import main_function, create_player


def test_should_return_perimeter(mocker):
    mocker.patch.object(circle, 'PI', 3.14)
    expected_value = 12.56
    assert perimeter(2) == expected_value




def test_main_function(mocker):
    mocker.patch('main.request', return_value=100)

    expected_value = 100
    assert main_function() == expected_value



class MockResponse:

    @staticmethod
    def get_info():
        return {"name": "test", "level": 200}


def test_create_player(mocker):
    mocker.patch('main.Player', return_value=MockResponse())

    expected_value = {"name": "test", "level": 200}
    assert create_player() == expected_value