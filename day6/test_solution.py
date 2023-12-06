from main import solve
from input_parser import parse_input_file

TEST_FILEPATH = "day6/example_input.txt"
EXPECTED_SOLUTION = 288


def test_solve():
    races = parse_input_file(TEST_FILEPATH)
    actual_solution = solve(races)
    print(actual_solution)
    try:
        assert actual_solution == EXPECTED_SOLUTION
        print("TEST PASSED")
    except:
        print("TEST FAILED")

if __name__ == '__main__':
    test_solve()
