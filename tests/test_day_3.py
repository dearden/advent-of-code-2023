from src.day_3 import get_numbers_adjacent_to_symbols, get_all_gears, calculate_gear_ratios, Gear
from pytest import mark


test_data_1 = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


@mark.parametrize("line_strings,expected", [(test_data_1, 4361)])
def test_get_numbers_adjacent_to_symbols(line_strings: list[str], expected: int):
    adj_nums = get_numbers_adjacent_to_symbols(test_data_1)
    assert sum(adj_nums) == expected


@mark.parametrize("line_strings,expected", [(test_data_1, 467835)])
def test_get_all_gears(line_strings: list[str], expected: int):
    gears: list[Gear] = get_all_gears(line_strings)
    gear_ratios: list[int] = calculate_gear_ratios(gears)
    assert sum(gear_ratios) == expected