import re


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
        return 2**(num_matches-1) if num_matches else 0
    

def get_card_value(card_string: str) -> int:
    card: Card = Card(card_string)
    return card.get_value()


def main():
    total = 0
    with open("data/day_4.txt") as in_file:
        for line in in_file:
            total += get_card_value(card_string=line)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
