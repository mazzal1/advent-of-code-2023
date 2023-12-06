from input_parser import parse_input_file
import math

INPUT_FILEPATH = "day5/input.txt"


def apply_map(map: list[dict[str, int]], source: int):
    destination = None
    for range_map in map:
        source_range_start = range_map["source_start"]
        source_range_end = range_map["source_start"] + range_map["range_length"]
        destination_range_start = range_map["destination_start"]
        if source in range(source_range_start, source_range_end):
            offset = source - source_range_start
            destination = destination_range_start + offset
            break
    if destination is None:
        destination = source
    return destination


def find_seed_location(problem, seed: int):
    soil = apply_map(problem["seed-to-soil"], seed)
    fertilizer = apply_map(problem["soil-to-fertilizer"], soil)
    water = apply_map(problem["fertilizer-to-water"], fertilizer)
    light = apply_map(problem["water-to-light"], water)
    temperature = apply_map(problem["light-to-temperature"], light)
    humidity = apply_map(problem["temperature-to-humidity"], temperature)
    location = apply_map(problem["humidity-to-location"], humidity)
    return location


def solve(problem):
    locations = []
    for seed in problem["seeds"]:
        location = find_seed_location(problem, seed)
        locations.append(location)
    solution = min(locations)
    return solution


def main():
    races = parse_input_file(INPUT_FILEPATH)
    solution = solve(races)
    print(solution)


if __name__ == '__main__':
    main()
