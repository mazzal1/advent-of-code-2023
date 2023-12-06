from main import solve
from input_parser import parse_input_file

TEST_FILEPATH = "day5b/example_input.txt"
EXPECTED_SOLUTION = 46


def test_solve():
    problem = parse_input_file(TEST_FILEPATH)
    actual_solution = solve(problem)
    print(actual_solution)
    try:
        assert actual_solution == EXPECTED_SOLUTION
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == '__main__':
    test_solve()
