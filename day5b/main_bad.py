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
    best_location = math.inf
    total_number_of_seeds = 0
    for seed_range in problem["seeds"]:
        total_number_of_seeds += seed_range["seed_range_length"]
    print(f"total number of seeds: {total_number_of_seeds}")
    processed_seeds = 0
    time_start = time()
    for seed_range in problem["seeds"]:
        seed_range_start = seed_range["seed_range_start"]
        seed_range_end = seed_range["seed_range_start"] + seed_range[
            "seed_range_length"]
        for seed in range(seed_range_start, seed_range_end):
            location = find_seed_location(problem, seed)
            if location < best_location:
                best_location = location
        processed_seeds += seed_range["seed_range_length"]
        time_checkpoint = time()
        elapsed_time = time_checkpoint - time_start
        eta = (elapsed_time / processed_seeds) * (total_number_of_seeds -
                                                  processed_seeds)
        estimated_total_time = (elapsed_time /
                                processed_seeds) * (total_number_of_seeds)
        print(
            f"progress: {processed_seeds / total_number_of_seeds * 100}% - eta: {eta} - estimated total time: {estimated_total_time}"
        )
    solution = best_location
    return solution


def main():
    problem = parse_input_file(INPUT_FILEPATH)
    solution = solve(problem)
    print(solution)


if __name__ == '__main__':
    main()
