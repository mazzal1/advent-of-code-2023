def parse_input_file(filepath: str):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return parse_input(lines)


def parse_input(lines: list[str]):
    problem = {
        "seeds": [],
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": []
    }
    parser_state = "seeds"
    for line in lines:
        if (line.startswith("seeds:")):
            seeds = line.lstrip("seeds: ").rstrip("\n")
            seeds = seeds.split(" ")
            seeds = filter(lambda x: x != '', seeds)
            seeds = list(map(int, seeds))
            problem["seeds"] = seeds
            continue
        if (line.startswith("seed-to-soil")):
            parser_state = "seed-to-soil"
            continue
        if (line.startswith("soil-to-fertilizer")):
            parser_state = "soil-to-fertilizer"
            continue
        if (line.startswith("fertilizer-to-water")):
            parser_state = "fertilizer-to-water"
            continue
        if (line.startswith("water-to-light")):
            parser_state = "water-to-light"
            continue
        if (line.startswith("light-to-temperature")):
            parser_state = "light-to-temperature"
            continue
        if (line.startswith("temperature-to-humidity")):
            parser_state = "temperature-to-humidity"
            continue
        if (line.startswith("humidity-to-location")):
            parser_state = "humidity-to-location"
            continue
        if line == '\n':
            continue
        line = line.rstrip('\n')
        (destination_start, source_start,
         range_length) = list(map(int, line.split(" ")))
        match parser_state:
            case "seeds":
                pass
            case "seed-to-soil":
                problem["seed-to-soil"].append({
                    "destination_start": destination_start,
                    "source_start": source_start,
                    "range_length": range_length
                })
            case "soil-to-fertilizer":
                problem["soil-to-fertilizer"].append({
                    "destination_start":
                    destination_start,
                    "source_start":
                    source_start,
                    "range_length":
                    range_length
                })
            case "fertilizer-to-water":
                problem["fertilizer-to-water"].append({
                    "destination_start":
                    destination_start,
                    "source_start":
                    source_start,
                    "range_length":
                    range_length
                })
            case "water-to-light":
                problem["water-to-light"].append({
                    "destination_start": destination_start,
                    "source_start": source_start,
                    "range_length": range_length
                })
            case "light-to-temperature":
                problem["light-to-temperature"].append({
                    "destination_start":
                    destination_start,
                    "source_start":
                    source_start,
                    "range_length":
                    range_length
                })
            case "temperature-to-humidity":
                problem["temperature-to-humidity"].append({
                    "destination_start":
                    destination_start,
                    "source_start":
                    source_start,
                    "range_length":
                    range_length
                })
            case "humidity-to-location":
                problem["humidity-to-location"].append({
                    "destination_start":
                    destination_start,
                    "source_start":
                    source_start,
                    "range_length":
                    range_length
                })
            case _:
                pass

    return problem
