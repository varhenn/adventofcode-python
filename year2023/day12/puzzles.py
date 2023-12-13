#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/12"""
from pathlib import Path
from functools import cache


def read_data(filepath: Path) -> list[tuple[str, tuple]]:
    with open(filepath) as file:
        rows = [x.split() for x in file.read().splitlines()]
    return [(d, tuple(map(int, s.split(",")))) for d, s in rows]


def first_puzzle(records: list[tuple[str, tuple]]) -> int:
    @cache
    def calc(d: str, s: tuple) -> int:
        if len(s) == 0:
            return "#" not in d
        d = d.lstrip(".")
        if (n := s[0]) < len(d):
            a = calc(d[n + 1:], s[1:]) if "." not in d[:n] and d[n] != "#" else 0
            b = calc(d[1:], s) if d[0] == "?" else 0
            return a + b
        return 0

    calc.cache_clear()
    return sum(calc(d + ".", s) for d, s in records)


def second_puzzle(records: list[tuple[str, tuple]]) -> int:
    return first_puzzle([("?".join([d] * 5), s * 5) for d, s in records])


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
