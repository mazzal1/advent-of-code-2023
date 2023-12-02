## Game 1: 4 blue, 7 red, 5 green; 3 blue, 4 red, 16 green; 3 red, 11 green


def parse_input(lines: list[str]) -> dict[int, list[dict[str, int]]]:
    games = {}
    for i, line in enumerate(lines):
        parts1 = line.rstrip().split(":")
        extractions_str = parts1[1]
        id = i+1
        extractions_list = []
        extractions_parts = extractions_str.split(";")
        for extraction in extractions_parts:
            extraction_dict = {}
            cube_sets = extraction.split(",")
            for cube_set in cube_sets:
                cube_set = cube_set.lstrip()
                [cubes_count, color] = cube_set.split(" ")
                cubes_count = int(cubes_count)
                extraction_dict[color] = cubes_count
            extractions_list.append(extraction_dict)
        games[id] = extractions_list
    return games


def parse_input_file(filepath: str) -> dict[int, list[dict[str, int]]]:
    with open(filepath, 'r') as file:
        lines = file.readlines()
    games = parse_input(lines)
    return games


test_games = ["Game 1: 4 blue, 7 red, 5 green; 3 blue, 4 red, 16 green; 3 red, 11 green"]
test_game_parsed = {
    1: [
        {
            "blue": 4,
            "red": 7,
            "green": 5
        },
        {
            "blue": 3,
            "red": 4,
            "green": 16
        },
        {
            "red": 3,
            "green": 11
        }
    ]
}


def test_parse_input():
    actual = parse_input(test_games)
    expected = test_game_parsed
    try:
        assert(actual == expected)
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == '__main__':
    test_parse_input()
