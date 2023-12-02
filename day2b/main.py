from parse_input import parse_input_file

INPUT_FILEPATH = "day2/input.txt"


def compute_fewest_cubes(game_extractions: list[dict[str, int]]) -> dict[str, int]:
    fewest_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for extraction in game_extractions:
        if "red" in extraction and extraction["red"] > fewest_cubes["red"]:
            fewest_cubes["red"] = extraction["red"]
        if "green" in extraction and extraction["green"] > fewest_cubes["green"]:
            fewest_cubes["green"] = extraction["green"]
        if "blue" in extraction and extraction["blue"] > fewest_cubes["blue"]:
            fewest_cubes["blue"] = extraction["blue"]
    return fewest_cubes


def compute_game_power(game_extractions: list[dict[str, int]]) -> int:
    fewest_cubes = compute_fewest_cubes(game_extractions)
    game_power = fewest_cubes["red"] * fewest_cubes["green"] * fewest_cubes["blue"]
    return game_power


def solve(games) -> int:
    power_sum = 0
    for id, extractions_list in games.items():
        game_power = compute_game_power(extractions_list)
        power_sum += game_power
    return power_sum


def main():
    games = parse_input_file(INPUT_FILEPATH)
    solution = solve(games)
    print(solution)


if __name__ == '__main__':
    main()
