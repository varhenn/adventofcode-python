#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/13"""
from pathlib import Path


def read_data(filepath: Path) -> list[list[str]]:
    with open(filepath) as file:
        return [p.splitlines() for p in file.read().split("\n\n")]


def first_puzzle(patterns: list[list[str]], errors: int = 0) -> int:
    def calc(p) -> int:
        for i in range(1, len(p)):
            chars = (cs for ls in zip(p[i-1::-1], p[i:]) for cs in zip(*ls))
            if sum(c1 != c2 for c1, c2 in chars) == errors:
                return i
        return 0

    return sum(100 * calc(p) + calc(list(zip(*p))) for p in patterns)


def second_puzzle(patterns: list[list[str]]) -> int:
    return first_puzzle(patterns, errors=1)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
