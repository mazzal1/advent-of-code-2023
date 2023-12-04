from input_parser import parse_input_file

INPUT_FILEPATH = "day4b/input.txt"


def get_number_of_card_winning_numbers(card_numbers, winning_numbers):
    sum = 0
    for card_number in card_numbers:
        if card_number in winning_numbers:
           sum += 1
    return sum 


def solve(cards: dict[int, dict[str, list[int] or int]]):
    for card_number, card in cards.items():
        number_of_winning_numbers = get_number_of_card_winning_numbers(card["card_numbers"], card["winning_numbers"])
        multiplicity = card["card_copies"]
        for i in range(1, number_of_winning_numbers + 1):
            if card_number + i in cards:
                cards[card_number + i]["card_copies"] += multiplicity
    sum_of_card_copies = 0
    for card in cards.values():
        sum_of_card_copies += card["card_copies"]
    return sum_of_card_copies


def main():
    cards = parse_input_file(INPUT_FILEPATH)
    solution = solve(cards)
    print(solution)


if __name__ == '__main__':
    main()
