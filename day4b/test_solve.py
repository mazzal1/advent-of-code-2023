from input_parser import parse_input_file
from main import solve

TEST_INPUT_FILEPATH = "day4/test_input.txt"


def test_solution():
    cards = parse_input_file(TEST_INPUT_FILEPATH)
    actual_solution = solve(cards)
    print(actual_solution)
    expected_solution = 30
    try:
        assert actual_solution == expected_solution
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == '__main__':
    test_solution()
