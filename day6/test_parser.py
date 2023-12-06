from input_parser import parse_input_file

TEST_FILEPATH = "day6/example_input.txt"

expected_problem = [
    {"time": 7, "distance": 9},
    {"time": 15, "distance": 40},
    {"time": 30, "distance": 200},
]


def test_parse_input_file():
    actual_problem = parse_input_file(TEST_FILEPATH)
    try:
        assert actual_problem == expected_problem
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == "__main__":
    test_parse_input_file()
    