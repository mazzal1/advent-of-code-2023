from input_parser import parse_input_file
import math
from time import time

INPUT_FILEPATH = "day5b/input.txt"


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


def find_range_map(map: list[dict[str, int]], source: int):
    for range_map in map:
        source_range_start = range_map["source_start"]
        source_range_end = range_map["source_start"] + range_map["range_length"]
        if source in range(source_range_start, source_range_end):
            return range_map
    return None


def find_none_range_length(map: list[dict[str, int]], source: int):
    end = math.inf
    for range_map in map:
        source_range_start = range_map["source_start"]
        if source_range_start > source and source_range_start < end:
            end = source_range_start
    return end - source


def map_ranges(ranges: list[dict[str, int]],
               map: list[dict[str, int]]) -> list[dict[str, int]]:
    mapped_ranges = []
    for range in ranges:
        range_start = range["range_start"]
        range_length = range["range_length"]
        range_end = range_start + range_length
        range_checkpoint = range_start
        while (range_checkpoint < range_end):
            range_map = find_range_map(map, range_checkpoint)
            mapped_range_start = apply_map(map, range_checkpoint)
            if (range_map == None):
                max_mapped_range_length = find_none_range_length(
                    map, mapped_range_start)
            else:
                max_mapped_range_length = range_map[
                    "destination_start"] + range_map[
                        "range_length"] - mapped_range_start
            mapped_range_length = min(
                [range_end - range_checkpoint, max_mapped_range_length])
            mapped_ranges.append({
                "range_start": mapped_range_start,
                "range_length": mapped_range_length
            })
            range_checkpoint = range_checkpoint + mapped_range_length
    return mapped_ranges


def find_location_ranges(seed_ranges: list[dict[str, int]],
                         problem) -> list[dict[str, int]]:
    print(f"{seed_ranges=}")
    soil_ranges = map_ranges(seed_ranges, problem["seed-to-soil"])
    print(f"{soil_ranges=}")
    fertilizer_ranges = map_ranges(soil_ranges, problem["soil-to-fertilizer"])
    print(f"{fertilizer_ranges=}")
    water_ranges = map_ranges(fertilizer_ranges,
                              problem["fertilizer-to-water"])
    print(f"{water_ranges=}")
    light_ranges = map_ranges(water_ranges, problem["water-to-light"])
    print(f"{light_ranges=}")
    temperature_ranges = map_ranges(light_ranges,
                                    problem["light-to-temperature"])
    print(f"{temperature_ranges=}")
    humidity_ranges = map_ranges(temperature_ranges,
                                 problem["temperature-to-humidity"])
    print(f"{humidity_ranges=}")
    location_ranges = map_ranges(humidity_ranges,
                                 problem["humidity-to-location"])
    print(f"{location_ranges=}")
    return location_ranges


def find_min_location(location_ranges: list[dict[str, int]]) -> int:
    min_location = min(range["range_start"] for range in location_ranges)
    return min_location


def solve(problem):
    seed_ranges = problem["seeds"]
    location_ranges = find_location_ranges(seed_ranges, problem)
    min_location = find_min_location(location_ranges)
    solution = min_location
    return solution


def main():
    problem = parse_input_file(INPUT_FILEPATH)
    solution = solve(problem)
    print(solution)


if __name__ == '__main__':
    main()
