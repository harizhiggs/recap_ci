from test_ci_project.game import greet
import re

def test_greet(capsys):
    greet("any_input_string")
    captured = capsys.readouterr()
    expected_pattern = re.compile(r"Hello, .+!")
    assert expected_pattern.search(captured.out), f"Expected pattern not found in output: {captured.out}"
