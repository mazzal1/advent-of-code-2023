from main import solve
from parse_input import parse_input_file


TEST_SOLUTION = 2286


def test_solve():
    games = parse_input_file("day2/test_input.txt")
    actual_solution = solve(games)
    expected_solution = TEST_SOLUTION
    try:
        assert actual_solution == expected_solution
        print("TEST_PASSED")
    except:
        print("TEST_FAILED")


def run_tests():
    test_solve()


if __name__ == '__main__':
    run_tests()
