def main():
    with open("day1/input.txt", 'r') as file:
        lines = file.readlines()
    sum = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                digit1 = char
                break
        for char in line[::-1]:
            if char.isdigit():
                digit2 = char
                break
        number = int("".join([digit1, digit2]))
        sum += number
    print(sum)


if __name__ == "__main__":
    main()
