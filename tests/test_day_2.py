from src.day_2 import get_all_possible_games, get_minimum_balls, get_power
from pytest import mark


test_data_1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

total_cubes_1 = {"red": 12, "green": 13, "blue": 14}


@mark.parametrize("games,total_cubes,expected", [(test_data_1, total_cubes_1, 8)])
def test_possible_games(games: list[str], total_cubes: dict[str, int], expected: int):
    possible_games = get_all_possible_games(games, total_cubes)
    assert sum(possible_games) == expected


@mark.parametrize(
    "game,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            {"red": 4, "green": 2, "blue": 6},
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            {"red": 1, "green": 3, "blue": 4},
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            {"red": 20, "green": 13, "blue": 6},
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            {"red": 14, "green": 3, "blue": 15},
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            {"red": 6, "green": 3, "blue": 2},
        ),
    ],
)
def test_minimum_balls(game: str, expected: dict[str, int]):
    min_balls = get_minimum_balls(game)
    for colour in expected:
        assert min_balls[colour] == expected[colour]



@mark.parametrize("games,expected", [(test_data_1, 2286)])
def test_get_power(games: list[str], expected: int):
    power = [get_power(game) for game in games]
    assert sum(power) == expected
