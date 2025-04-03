import circle
from circle import perimeter


def test_should_return_perimeter(mocker):
    mocker.patch.object(circle, 'PI', 3.14)
    expected_value = 12.56
    assert perimeter(2) == expected_value