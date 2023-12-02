from parse_input import parse_input_file

INPUT_FILEPATH = "day2/input.txt"

BOUNDARIES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_extraction_possible(extraction: dict[str, int], boundaries: dict[str, int]) -> bool:
    is_red_possible = extraction["red"] <= boundaries["red"] if "red" in extraction else True
    is_green_possible = extraction["green"] <= boundaries["green"] if "green" in extraction else True
    is_blue_possible = extraction["blue"] <= boundaries["blue"] if "blue" in extraction else True
    is_possible = all([is_red_possible, is_green_possible, is_blue_possible])
    return is_possible


def is_game_possible(game_extractions: list[dict[str, int]], boundaries: dict[str, int]) -> bool:
    def extractions_are_possible(extraction: dict[str, int]):
        return is_extraction_possible(extraction, boundaries)
    
    is_possible = all(map(extractions_are_possible, game_extractions))
    return is_possible


def solve(games, boundaries) -> int:
    id_sum = 0
    for id, exrtactions_list in games.items():
        is_possible = is_game_possible(exrtactions_list, boundaries)
        if is_possible:
            id_sum += id
    return id_sum


def main():
    games = parse_input_file(INPUT_FILEPATH)
    solution = solve(games, boundaries=BOUNDARIES)
    print(solution)


if __name__ == '__main__':
    main()
