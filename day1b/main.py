string_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
string_digits_dict= {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def find_digit(line: str, reverse=False) -> str:
    digit: str = None
    buffer=""
    if reverse:
        line = line[::-1]
    for char in line:
        if char.isdigit():
            digit = char
            break
        else:
            buffer = buffer + char
            for string_digit in string_digits:
                if not reverse:
                    index = buffer.find(string_digit)
                else:
                    index = buffer[::-1].find(string_digit)
                if index != -1:
                    digit = string_digits_dict[string_digit]
                    break
            if digit is not None:
                break
    if (digit is None):
        raise Exception(f"Digit not found in {line=}")
    return digit


def find_number(line: str):
    digit1 = find_digit(line)
    digit2 = find_digit(line, reverse=True)
    number = int("".join([digit1, digit2]))
    return number


def main():
    with open("day1b/input.txt", 'r') as file:
        lines = file.readlines()
    sum = 0
    for line in lines:
        number = find_number(line)
        sum += number
    print(sum)


def test_find_digit():
    test_line = "fivethreeonezblqnsfk1"
    digit1 = find_digit(test_line)
    digit2 = find_digit(test_line, reverse=True)
    if digit1 == "5" and digit2 == "1":
        print("test SUCCESS")
    else:
        print("test FAIL")


def test_find_number():
    test_data = {
        "two1nine": 29,
        "eightwothree": 83,
        "abcone2threexyz": 13, 
        "xtwone3four": 24, 
        "4nineeightseven2": 42, 
        "zoneight234": 14, 
        "7pqrstsixteen": 76
    }
    try:
        for (line, solution) in test_data.items():
            assert(find_number(line) == solution)
        print("test SUCCESS")
    except:
        print("test FAIL")


if __name__ == "__main__":
    main()
