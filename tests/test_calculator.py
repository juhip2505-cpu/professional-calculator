from unittest.mock import patch
from app.calculator.calculator import Calculator


def test_show_help(capsys):
    calculator = Calculator()
    calculator.show_help()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "exit" in captured.out


def test_show_history_empty(capsys):
    calculator = Calculator()
    calculator.show_history()
    captured = capsys.readouterr()
    assert "No calculations yet." in captured.out


def test_show_history_with_items(capsys):
    calculator = Calculator()
    calculator.history.append("add(1.0, 2.0) = 3.0")
    calculator.show_history()
    captured = capsys.readouterr()
    assert "add(1.0, 2.0) = 3.0" in captured.out


def test_run_exit(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Professional Calculator" in captured.out
    assert "Goodbye!" in captured.out


def test_run_help(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["help", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Available commands:" in captured.out


def test_run_history(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["history", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "No calculations yet." in captured.out


def test_run_invalid_command(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["banana", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Invalid command." in captured.out


def test_run_add(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["add", "2", "3", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_run_invalid_number(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["add", "hello", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Invalid number entered." in captured.out


def test_run_divide_by_zero(capsys):
    calculator = Calculator()

    with patch("builtins.input", side_effect=["divide", "10", "0", "exit"]):
        calculator.run()

    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out 