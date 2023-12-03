from problem_parser import parse_input_file
from main import solve

TEST_INPUT_FILEPATH = "day3/example_input.txt"
EXPECTED_SOLUTION = 4361


def test_solve():
    schematic = parse_input_file(TEST_INPUT_FILEPATH)
    actual_solution = solve(schematic)
    expected_solution = EXPECTED_SOLUTION
    print(actual_solution)
    print(expected_solution)
    try:
        assert actual_solution == expected_solution
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == "__main__":
    test_solve()
