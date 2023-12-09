#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/4"""
from collections import defaultdict
from pathlib import Path
from re import findall
from functools import reduce
from operator import and_


def read_data(filepath: Path) -> list[int]:
    """Returns number of winning numbers on each card"""
    pattern = r"Card +\d+: ([\d ]+) \| ([\d ]+)"
    with open(filepath) as file:
        return [
            len(reduce(and_, [set(p.split()) for p in c]))
            for c in findall(pattern, file.read())
        ]


def first_puzzle(cards: list[int]) -> int:
    return sum(2 ** (wins - 1) for wins in cards if wins)


def second_puzzle(cards: list[int]) -> int:
    scratchcards = defaultdict(lambda: 1)
    for card, wins in enumerate(cards, 1):
        copies = scratchcards[card]
        for idx in range(card + 1, card + wins + 1):
            scratchcards[idx] += copies
    return sum(scratchcards.values())


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
