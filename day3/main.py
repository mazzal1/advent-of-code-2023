from problem_parser import parse_input_file
from typing import Any

INPUT_FILEPATH = "day3/input.txt"


def is_adjacent_to_symbol(number_meta: dict[str, int], symbols: dict[int, list[dict[str, Any]]]):
    number_line: int = number_meta["line"]
    for line in range(number_line-1,number_line+2):
        if line in symbols:
            for symbol_meta in symbols[line]:
                if symbol_meta["column"] in range(number_meta["first_column"]-1, number_meta["last_column"] + 2):
                    return True
                

def solve(schematic: dict[str, dict[int, list[dict[str, Any]]]]) -> int:
    sum = 0
    for number_list in schematic["numbers"].values():
        for number_meta in number_list:
            if (is_adjacent_to_symbol(number_meta, schematic["symbols"])):
                sum += number_meta["number"]
    return sum


def main():
    schematic = parse_input_file(INPUT_FILEPATH)
    solution = solve(schematic)
    print(solution)


if __name__ == "__main__":
    main()
