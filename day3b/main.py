from problem_parser import parse_input_file
from typing import Any

INPUT_FILEPATH = "day3b/input.txt"


def get_adjacent_numbers(symbol_meta: dict[str, int], numbers: dict[int, list[dict[str, Any]]]):
    symbol_line: int = symbol_meta["line"]
    adjacent_numbers = []
    for line in range(symbol_line-1,symbol_line+2):
        if line in numbers:
            for number_meta in numbers[line]:
                if symbol_meta["column"] in range(number_meta["first_column"]-1, number_meta["last_column"] + 2):
                    adjacent_numbers.append(number_meta)
    return adjacent_numbers


def compute_gear_power(symbol_meta: dict[str, int], numbers: dict[int, list[dict[str, Any]]]) -> bool:
    if (symbol_meta["symbol"] != '*'):
        return 0
    adjacent_numbers = get_adjacent_numbers(symbol_meta, numbers)
    if len(adjacent_numbers) != 2:
        return 0
    return adjacent_numbers[0]["number"] * adjacent_numbers[1]["number"]
                

def solve(schematic: dict[str, dict[int, list[dict[str, Any]]]]) -> int:
    sum = 0
    for symbol_list in schematic["symbols"].values():
        for symbol_meta in symbol_list:
            gear_power = compute_gear_power(symbol_meta, schematic["numbers"])
            sum += gear_power
    return sum


def main():
    schematic = parse_input_file(INPUT_FILEPATH)
    solution = solve(schematic)
    print(solution)


if __name__ == "__main__":
    main()
