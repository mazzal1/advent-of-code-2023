from input_parser import parse_input_file

INPUT_FILEPATH = "day6/input.txt"


def compute_number_of_winning_setups(time: int, record: int):
    number_of_winning_setups = 0
    for i in range(time+1):
        speed = i
        remaining_time = time - i
        distance = speed * remaining_time
        if distance > record:
            number_of_winning_setups += 1
    return number_of_winning_setups


def solve(races: list[dict[str, int]]):
    solution = 1
    for race in races:
        number_of_winning_setups = compute_number_of_winning_setups(time=race["time"], record=race["distance"])
        solution *= number_of_winning_setups
    return solution


def main():
    races = parse_input_file(INPUT_FILEPATH)
    solution = solve(races)
    print(solution)


if __name__ == '__main__':
    main()
