import pytest

from services import Parser


@pytest.fixture(scope="function")
def mock_parser(request, monkeypatch):
    parser = Parser()

    def mock_set_expression(self):
        self.expression = request.param
    monkeypatch.setattr(Parser, "set_expression", mock_set_expression)
    parser.set_expression()
    return parser


@pytest.mark.parametrize("mock_parser, expected_result", [("3+1", 4)],
                         indirect=["mock_parser"])
def test_parser_evaluate(mock_parser, expected_result):
    actual_result = mock_parser.evaluate_expression()
    assert actual_result == expected_result


@pytest.mark.parametrize("mock_parser, expected_result", [("3+1", True)],
                         indirect=["mock_parser"])
def test_parser_check(mock_parser, expected_result):
    actual_result = mock_parser.check_expression()
    assert actual_result == expected_result
