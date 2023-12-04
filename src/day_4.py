import re
from typing import Iterator


CARD_REGEX = re.compile(r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)")


class Card:
    def __init__(self, card_string: str) -> None:
        m = CARD_REGEX.match(card_string.strip())
        self.card_num = int(m.group(1))
        self.winning = set([int(n) for n in list(m.group(2).split(" ")) if len(n)])
        self.you_have = set([int(n) for n in list(m.group(3).split(" ")) if len(n)])

    def get_your_winning_numbers(self) -> set[int]:
        return self.winning.intersection(self.you_have)

    def get_value(self) -> int:
        num_matches = len(self.get_your_winning_numbers())
        return 2 ** (num_matches - 1) if num_matches else 0


def read_card_file() -> Iterator[Card]:
    with open("data/day_4.txt") as in_file:
        for line in in_file:
            yield Card(card_string=line)


def get_cards_won(iter_cards: Iterator[Card]) -> int:
    card_match_dict = {
        card.card_num: len(card.get_your_winning_numbers()) for card in iter_cards
    }

    total_won = 0

    def number_of_cards_won(cur_card: int) -> int:
        num_cards_won = card_match_dict.get(cur_card, 0)
        if num_cards_won > 0:
            cards_won = list(range(cur_card + 1, cur_card + num_cards_won + 1))
            return num_cards_won + sum((number_of_cards_won(num) for num in cards_won))
        else:
            return 0

    for cur_card in card_match_dict:
        total_won += number_of_cards_won(cur_card) + 1

    return total_won


def main():
    # Part one
    total = sum((card.get_value() for card in read_card_file()))
    print(f"Total: {total}")

    # Part two
    num_cards_won = get_cards_won(read_card_file())
    print(f"Cards won: {num_cards_won}")


if __name__ == "__main__":
    main()
