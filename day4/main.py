from input_parser import parse_input_file

INPUT_FILEPATH = "day4/input.txt"


def solve(cards: list[dict[str, list[int]]]):
    sum = 0
    for card in cards:
        card_winning_numbers = 0
        for card_number in card["card_numbers"]:
            if card_number in card["winning_numbers"]:
                card_winning_numbers += 1
        if card_winning_numbers > 0:
            card_points = 2 ** (card_winning_numbers - 1)
            print(card_points)
            sum += card_points
    return sum


def main():
    cards = parse_input_file(INPUT_FILEPATH)
    solution = solve(cards)
    print(solution)


if __name__ == '__main__':
    main()
