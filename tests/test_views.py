from textwrap import dedent

from calculate.view import View
def test_print_menu(capsys):
    View.print_menu()
    captured = capsys.readouterr()
    expected_out = dedent("""
    =========== MENU ===========
    1 - Addition
    2 - Soustraction
    3 - Multiplication
    4 - Division
    5 - Quitter
    ============================\n
    """)
    assert captured.out == expected_out


def test_get_user_input(monkeypatch):
    message ="Bonjour"
    monkeypatch.setattr('builtins.input', lambda _: message)
    assert View.get_user_input(message) == 'Bonjour'

def test_end_message(capsys):
    View.end_message()
    expected_out = dedent("""
    =========== GOOD-BYE ===========
    """)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_out.strip()

def test_continue_message(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "")
    View.continue_message()
    assert True