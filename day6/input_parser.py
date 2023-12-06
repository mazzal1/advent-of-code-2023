def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return parse_input(lines)


def parse_input(lines: list[str]):
    times = lines[0].lstrip("Time: ").rstrip("\n").split(" ")
    times = filter(lambda x: x != '', times)
    times = list(map(int, times))
    print(times)
    distances = lines[1].lstrip("Distance: ").split(" ")
    distances = filter(lambda x: x != '', distances)
    distances = list(map(int, distances))
    print(distances)
    races = []
    for (time, distance) in zip(times, distances):
        races.append({
            "time": time,
            "distance": distance
        })
    return races
