from functools import cmp_to_key
from enum import Enum
from collections import Counter


input = open("./input.txt", "r").read()


def main():
    hands = parse(input)
    hands.sort(key=cmp_to_key(compare_hands))
    output = 0
    for i, hand in enumerate(hands):
        output += (i + 1) * hand.bid
    return output


def parse(input):
    input = input.split('\n')
    output = []
    for line in input:
        output.append(Hand(line))
    return output


class Hand:
    def __init__(self, line) -> None:
        [cards, bid] = line.split()
        self.bid = int(bid)
        self.type_ = HandType.from_cards(cards)
        cards = list(cards)
        for i, card in enumerate(cards):
            cards[i] = Card.from_char(card)
        self.cards = cards
        print(self.cards)


def compare_hands(a, b) -> int:
    if a.type_.value > b.type_.value:
        return 1
    if a.type_.value < b.type_.value:
        return -1
    for i in range(5):
        if a.cards[i].value > b.cards[i].value:
            return 1
        if a.cards[i].value < b.cards[i].value:
            return -1
    return 0


class Card(Enum):
    A=13
    K=12
    Q=11
    T=10
    N9=9
    N8=8
    N7=7
    N6=6
    N5=5
    N4=4
    N3=3
    N2=2
    J =1

    def from_char(char):
        match char:
            case "A":
                return Card.A
            case "K":
                return Card.K
            case "Q":
                return Card.Q
            case "J":
                return Card.J
            case "T":
                return Card.T
            case "9":
                return Card.N9
            case "8":
                return Card.N8
            case "7":
                return Card.N7
            case "6":
                return Card.N6
            case "5":
                return Card.N5
            case "4":
                return Card.N4
            case "3":
                return Card.N3
            case "2":
                return Card.N2


class HandType(Enum):
    FIVE_OF_A_KIND  =7
    FOUR_OF_A_KIND  =6
    FULL_HOUSE      =5
    THREE_OF_A_KIND =4
    TWO_PAIR        =3
    ONE_PAIR        =2
    HIGH_CARD       =1

    def from_cards(cards):
        counter = Counter(cards)

        if counter["J"] > 0:
            if counter["J"] == 5:
                return HandType.FIVE_OF_A_KIND
            most_common = counter.most_common(1)[0][0]
            if most_common == "J":
                most_common = counter.most_common(2)[1][0]
            counter[most_common] += counter["J"]
            del counter["J"]

        if len(counter) == 1:
            return HandType.FIVE_OF_A_KIND
        if len(counter) == 2 and max(counter.values()) == 4:
            return HandType.FOUR_OF_A_KIND
        if len(counter) == 2 and max(counter.values()) == 3:
            return HandType.FULL_HOUSE
        if len(counter) == 3 and max(counter.values()) == 3:
            return HandType.THREE_OF_A_KIND
        if len(counter) == 3 and max(counter.values()) == 2:
            return HandType.TWO_PAIR
        if len(counter) == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD
        


print(main())
