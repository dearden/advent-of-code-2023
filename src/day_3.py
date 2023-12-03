import re

from math import prod
from dataclasses import dataclass


@dataclass(frozen=True)
class Number:
    number: int
    first: int
    last: int


@dataclass(frozen=True)
class Symbol:
    symbol: str
    position: int


@dataclass(frozen=True)
class Gear:
    numbers: list[int]


class Line:
    def __init__(self, line_string: str) -> None:
        self.numbers = [
            Number(int(m.group(0)), m.span()[0], m.span()[1] - 1)
            for m in NUMBER_REGEX.finditer(line_string)
        ]
        self.symbols = [
            Symbol(m.group(0), m.span()[0]) for m in SYMBOL_REGEX.finditer(line_string)
        ]

    def get_numbers_adjacent_to_symbols(
        self, before: "Line", after: "Line"
    ) -> list[Number]:
        adj_nums = []
        adj_nums += self.numbers_next_to_symbols(before.symbols)
        adj_nums += self.numbers_next_to_symbols(self.symbols)
        adj_nums += self.numbers_next_to_symbols(after.symbols)
        return list(set(adj_nums))

    def numbers_next_to_symbols(self, symbols: list[Symbol]) -> list[Number]:
        return [n for n in self.numbers if self.is_number_next_to_a_symbol(n, symbols)]
    
    def are_these_adjacent(self, n: Number, s: Symbol) -> bool:
        return s.position >= n.first - 1 and s.position <= n.last + 1

    def is_number_next_to_a_symbol(self, number: Number, symbols: list[Symbol]) -> bool:
        for s in symbols:
            if self.are_these_adjacent(number, s):
                return True
        return False
    
    def find_gears(self, before: "Line", after: "Line") -> list[Gear]:
        gears = []
        for symbol in self.symbols:
            numbers = []
            numbers += self.get_numbers_next_to_this_symbol(symbol, before.numbers)
            numbers += self.get_numbers_next_to_this_symbol(symbol, self.numbers)
            numbers += self.get_numbers_next_to_this_symbol(symbol, after.numbers)
            numbers = list(set(numbers))
            numbers = [n.number for n in numbers]
            if len(numbers) == 2:
                gears.append(Gear(numbers))
        return gears
    
    def get_numbers_next_to_this_symbol(self, symbol: Symbol, numbers: list[Number]):
        return [number for number in numbers if self.are_these_adjacent(number, symbol)]



SYMBOL_REGEX: re.Pattern = re.compile(r"[^0-9\.]")
NUMBER_REGEX: re.Pattern = re.compile(r"\d+")


def get_numbers_adjacent_to_symbols(line_strings: list[str]) -> list[int]:
    lines: list[Line] = [Line(l) for l in line_strings]

    adj_nums: list[Number] = []
    for i, line in enumerate(lines):
        before_line = lines[i - 1] if i > 0 else Line("")
        after_line = lines[i + 1] if i < len(lines) - 1 else Line("")
        adj_nums += line.get_numbers_adjacent_to_symbols(before_line, after_line)

    return [n.number for n in adj_nums]


def get_all_gears(line_strings: list[str]) -> list[int]:
    lines: list[Line] = [Line(l) for l in line_strings]

    gears: list[Gear] = []
    for i, line in enumerate(lines):
        before_line = lines[i - 1] if i > 0 else Line("")
        after_line = lines[i + 1] if i < len(lines) - 1 else Line("")
        gears += line.find_gears(before_line, after_line)

    return gears


def calculate_gear_ratios(gears: list[Gear]) -> list[int]:
    return [prod(gear.numbers) for gear in gears]


def main():
    with open("data/day_3.txt") as in_file:
        data = [l.strip() for l in in_file]

    adj_numbers: list[Number] = get_numbers_adjacent_to_symbols(data)
    print(f"Sum: {sum(adj_numbers)}")

    gears: list[Gear] = get_all_gears(data)
    gear_ratios: list[int] = calculate_gear_ratios(gears)
    print(f"Sum: {sum(gear_ratios)}")


if __name__ == "__main__":
    main()
