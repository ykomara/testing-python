import main
from main import main_function, create_player
def test_main_function(monkeypatch):
    def mockreturn():
        return 200
    monkeypatch.setattr(main, 'request', mockreturn)
    expected_value=200
    assert main_function()==expected_value


class MockResponse:

    @staticmethod
    def get_info():
        return {"name": "test", "level": 200}


def test_create_player(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr('main.Player', mock_get)

    expected_value = {"name": "test", "level": 200}
    assert create_player() == expected_value