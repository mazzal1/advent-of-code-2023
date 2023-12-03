from typing import Any

symbols = ["*", "#", "+", "$", "=", "/", "%", "@"]
not_symbols = ["a", "1", ".", "\n", "\0", "\t", " "]

test_input = ["467..114\n", "...*......\n"]

expected_schematic = {
    "numbers": {
        0: [
            {
               "number": 467,
               "line": 0,
               "first_column": 0,
               "last_column": 2
            },
            {
                "number": 114,
                "line": 0,
                "first_column": 5,
                "last_column": 7
            }
        ]
    },
    "symbols": {
        1: [
            {
                "symbol": "*",
                "line": 1,
                "column": 3
            }
        ]
    }
}


def is_symbol(char: str) -> bool:
    result = not char.isalnum() and not char.isspace() and char.isprintable() and not char == '.'
    return result


def append_number_to_schematic(schematic: dict[str, dict[int, list[dict[str, Any]]]], number_str: str, line: int, first_column: int, last_column: int):
    number = int(number_str)
    if not line in schematic["numbers"]:
        schematic["numbers"][line] = []
    number_list: list[dict[str, int]] = schematic["numbers"][line]
    number_entry = {
        "number": number,
        "line": line,
        "first_column": first_column,
        "last_column": last_column
    }
    number_list.append(number_entry)
    return schematic


def append_symbol_to_schematic(schematic: dict[str, dict[int, list[dict[str, Any]]]], symbol: str, line: int, column: int):
    if not line in schematic["symbols"]:
        schematic["symbols"][line] = []
    symbol_list: list[dict[str, int]] = schematic["symbols"][line]
    symbol_entry = {
        "symbol": symbol,
        "line": line,
        "column": column
    }
    symbol_list.append(symbol_entry)
    return schematic
    

def parse_input(lines: list[str]) -> dict[str, dict[int, list[dict[str, Any]]]]:
    schematic = {
        "numbers": {},
        "symbols": {}
    }
    for i, line in enumerate(lines):
        number = ""
        for j, char in enumerate(line):
            if char.isdigit():
                number = number + char
            if char == '.' or char == "\n" or is_symbol(char):
                if number != "": 
                    schematic = append_number_to_schematic(schematic, number, line=i, first_column=j-len(number), last_column=j-1)
                number = ""
            if is_symbol(char):
                schematic = append_symbol_to_schematic(schematic, char, line=i, column=j)
    return schematic


def parse_input_file(filename: str) -> dict[str, dict[int, list[dict[str, Any]]]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if (not line.endswith("\n")):
            lines[i] = line + "\n"
    schematic = parse_input(lines)
    return schematic


def test_is_symbol():
    try:
        for symbol in symbols:
            assert is_symbol(symbol)
        for not_symbol in not_symbols:
            assert not is_symbol(not_symbol)
        print("TEST PASSED")
    except:
        print("TEST FAILED")


def test_parse_input():
    try:
        actual_schematic = parse_input(test_input)
        print(actual_schematic)
        print(expected_schematic)
        assert actual_schematic == expected_schematic
        print("TEST_PASSED")
    except:
        print("TEST_FAILED")


def run_tests():
    test_is_symbol()
    test_parse_input()


if __name__ == "__main__":
    run_tests()
