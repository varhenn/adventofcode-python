#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/7"""
from collections import Counter
from pathlib import Path
from typing import NamedTuple


class Card(NamedTuple):
    hand: str
    bet: str


def read_data(filepath: Path) -> list[Card]:
    with open(filepath) as file:
        return [Card(*line.split()) for line in file.readlines()]


def _calc_total_winnings(cards: list[Card], use_jokers: bool) -> int:
    def strength(hand: str, use_jokers: bool) -> tuple:
        counter = Counter(hand)
        if use_jokers and 0 < (jokers := counter["J"]) < 5:
            del counter["J"]
            counter[counter.most_common(1)[0][0]] += jokers
        freq = sorted(counter.values(), reverse=True)
        card_order = "AKQT98765432J" if use_jokers else "AKQJT98765432"
        labels = [-card_order.index(c) for c in hand]
        return freq, *labels

    sorted_cards = sorted(cards, key=lambda c: strength(c.hand, use_jokers))
    return sum(r * int(c.bet) for r, c in enumerate(sorted_cards, 1))


def first_puzzle(cards: list[Card]) -> int:
    return _calc_total_winnings(cards, use_jokers=False)


def second_puzzle(cards: list[Card]) -> int:
    return _calc_total_winnings(cards, use_jokers=True)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
