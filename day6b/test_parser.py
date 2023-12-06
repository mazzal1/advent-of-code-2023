from input_parser import parse_input_file

TEST_FILEPATH = "day6b/example_input.txt"

expected_races = [
    {"time": 71530, "distance": 940200},
]


def test_parse_input_file():
    actual_races = parse_input_file(TEST_FILEPATH)
    try:
        assert actual_races == expected_races
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == "__main__":
    test_parse_input_file()
