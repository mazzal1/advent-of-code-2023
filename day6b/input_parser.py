def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return parse_input(lines)


def parse_input(lines: list[str]):
    times = lines[0].lstrip("Time: ").rstrip("\n").split(" ")
    times = filter(lambda x: x != '', times)
    time_str = ''.join(times)
    time = int(time_str)
    print(time)
    distances = lines[1].lstrip("Distance: ").split(" ")
    distances = filter(lambda x: x != '', distances)
    distance_str = ''.join(distances)
    distance = int(distance_str)
    print(distance)
    races = [{
            "time": time,
            "distance": distance
        }]
    return races
