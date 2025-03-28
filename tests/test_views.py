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


