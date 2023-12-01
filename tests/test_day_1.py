from src.day_1 import find_value, get_sum
from pytest import mark


@mark.parametrize(
    "text,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_find_value(text: str, expected: int):
    assert find_value(text) == expected


@mark.parametrize(
    "lines,expected",
    [
        (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142),
        (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
            281,
        ),
    ],
)
def test_get_sum(lines: list[str], expected: int):
    assert get_sum(lines) == expected
