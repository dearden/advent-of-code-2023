import re


string_digit_map: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_all_digits(text: str) -> list[str]:
    text_number_regex = re.compile(f"(?=({'|'.join(list(string_digit_map))}))")
    text = text_number_regex.sub(lambda match: string_digit_map[match.group(1)], text)
    digits = [c for c in text if c.isdigit()]
    return digits


def find_value(text: str) -> int:
    digits = get_all_digits(text)
    if len(digits) <= 0:
        return 0
    value = int(digits[0] + digits[-1])
    return value


def get_sum(lines: list[str]) -> int:
    values = [find_value(line) for line in lines]
    return sum(values)


def main():
    with open("data/day_1.txt") as in_file:
        data = [line.strip() for line in in_file]

    print(f"Sum: {get_sum(data)}")


if __name__ == "__main__":
    main()
