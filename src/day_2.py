import re
from math import prod


cube_count_regex = r"(\d+) ([a-zA-Z]+)"


def parse_cube_count(result_string) -> tuple[str, int]:
    result_string = result_string.strip()
    m = re.match(cube_count_regex, result_string.strip())
    colour = m.group(2)
    amount = int(m.group(1))
    return colour, amount


def parse_round(round_string: str) -> dict[str, int]:
    result_strings = round_string.split(",")
    round_count = {"red": 0, "green": 0, "blue": 0}
    for result_string in result_strings:
        result = parse_cube_count(result_string)
        round_count[result[0]] += result[1]
    return round_count


def check_if_possible(game_string: str, total_cubes: dict[str, int]) -> tuple[int, bool]:
    game_number, results = game_string.split(":")
    game_number = int(game_number.split(" ")[-1])
    rounds = results.split(";")
    game = [parse_round(r) for r in rounds]
    for colour, amount in total_cubes.items():
        for r in game:
            if r[colour] > amount:
                return game_number, False
    return game_number, True


def get_minimum_balls(game_string: str) -> dict[str, int]:
    _, results = game_string.split(":")
    rounds = results.split(";")
    game = [parse_round(r) for r in rounds]
    minimum_balls = {"red": 0, "green": 0, "blue": 0}
    for r in game:
        for colour, cur_min in minimum_balls.items():
            minimum_balls[colour] = max(cur_min, r[colour])
    return minimum_balls


def get_power(game_string: str) -> int:
    min_balls = get_minimum_balls(game_string)
    return prod(min_balls.values())


def get_all_possible_games(games: list[str], total_cubes: dict[str, int]) -> list[int]:
    checked_games = [check_if_possible(line, total_cubes) for line in games]
    possible_games = [g[0] for g in checked_games if g[1] == True]
    return possible_games


def main():
    with open("data/day_2.txt") as in_file:
        data = [line for line in in_file]
    
    total_cubes = {"red": 12, "green": 13, "blue": 14}
    
    possible_games = get_all_possible_games(data, total_cubes)

    print(f"Possible games sum: {sum(possible_games)}")

    powers = [get_power(line) for line in data]

    print(f"Minimum balls power: {sum(powers)}")


if __name__ == "__main__":
    main()