def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    cards = parse_input(lines)
    return cards


def parse_input(lines: list[str]):
    cards = {}
    for i, line in enumerate(lines):
        [_, numbers] = line.split(":")
        [winning_numbers_str, game_numbers_str] = numbers.split(" | ")
        winning_numbers_str = winning_numbers_str.lstrip(" ")
        game_numbers_str = game_numbers_str.rstrip("\n")
        winning_numbers = winning_numbers_str.split(" ")
        game_numbers = game_numbers_str.split(" ")
        winning_numbers = filter(lambda x: x != '', winning_numbers)
        game_numbers = filter(lambda x: x != '', game_numbers)
        winning_numbers = list(map(int, winning_numbers))
        game_numbers = list(map(int, game_numbers))
        card_number = i+1
        card_copies = 1
        card = {
            "card_number": card_number,
            "card_copies": card_copies,
            "winning_numbers": winning_numbers,
            "card_numbers": game_numbers
        }
        cards[card_number] = card
    return cards


def test_parse_input():
    actual_cards = parse_input(["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
                                "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"])
    expected_result = {
        1: {
            "card_number": 1,
            "card_copies": 1,
            "winning_numbers": [41, 48, 83, 86, 17],
            "card_numbers": [83, 86, 6, 31, 17, 9, 48, 53]
        },
        2: {
            "card_number": 2,
            "card_copies": 1,
            "winning_numbers": [13, 32, 20, 16, 61],
            "card_numbers": [61, 30, 68, 82, 17, 32, 24, 19]
        }
    }
    try:
        assert actual_cards == expected_result
        print("TEST PASSED")
    except:
        print("TEST FAILED")


if __name__ == '__main__':
    test_parse_input()
