from input_parser import parse_input_file

TEST_FILEPATH = "day5/example_input.txt"

expected_problem = {
    "seeds": [79, 14, 55, 13],
    "seed-to-soil": [{
        "destination_start": 50,
        "source_start": 98,
        "range_length": 2
    }, {
        "destination_start": 52,
        "source_start": 50,
        "range_length": 48
    }],
    "soil-to-fertilizer": [{
        "destination_start": 0,
        "source_start": 15,
        "range_length": 37
    }, {
        "destination_start": 37,
        "source_start": 52,
        "range_length": 2
    }, {
        "destination_start": 39,
        "source_start": 0,
        "range_length": 15
    }],
    'fertilizer-to-water': [{
        'destination_start': 49,
        'source_start': 53,
        'range_length': 8
    }, {
        'destination_start': 0,
        'source_start': 11,
        'range_length': 42,
    }, {
        'destination_start': 42,
        'source_start': 0,
        'range_length': 7
    }, {
        'destination_start': 57,
        'source_start': 7,
        'range_length': 4
    }],
    'water-to-light': [{
        'destination_start': 88,
        'source_start': 18,
        'range_length': 7
    }, {
        'destination_start': 18,
        'source_start': 25,
        'range_length': 70
    }],
    'light-to-temperature': [{
        'destination_start': 45,
        'source_start': 77,
        'range_length': 23
    }, {
        'destination_start': 81,
        'source_start': 45,
        'range_length': 19
    }, {
        'destination_start': 68,
        'source_start': 64,
        'range_length': 13
    }],
    'temperature-to-humidity': [{
        'destination_start': 0,
        'source_start': 69,
        'range_length': 1
    }, {
        'destination_start': 1,
        'source_start': 0,
        'range_length': 69
    }],
    'humidity-to-location': [{
        'destination_start': 60,
        'source_start': 56,
        'range_length': 37
    }, {
        'destination_start': 56,
        'source_start': 93,
        'range_length': 4
    }]
}


def test_parse_input_file():
    actual_problem = parse_input_file(TEST_FILEPATH)
    try:
        assert actual_problem == expected_problem
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == "__main__":
    test_parse_input_file()
