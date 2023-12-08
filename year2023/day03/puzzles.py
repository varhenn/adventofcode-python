#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/3"""
import math
from pathlib import Path
from re import finditer
from typing import Iterable

Symbols = dict[complex, str]  # coordinate: symbol
Numbers = dict[complex, tuple[complex, int]]  # coordinate: (unique id, value)


def read_data(filepath: Path) -> tuple[Symbols, Numbers]:
    tokens = {
        complex(x, y): (complex(x, t), m.group())
        for x, line in enumerate(open(filepath).read().splitlines())
        for t, m in enumerate(finditer(r"(\d+)|([^.])", line))
        for y in range(*m.span())
    }
    symbols = {p: v for p, (t, v) in tokens.items() if not v.isdigit()}
    numbers = {p: (t, int(v)) for p, (t, v) in tokens.items() if v.isdigit()}
    return symbols, numbers


def neighbours(point: complex) -> Iterable[complex]:
    for delta in (-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j):
        yield point + delta


def first_puzzle(symbols: Symbols, nums: Numbers) -> int:
    adj = dict(nums[n] for p in symbols.keys() for n in neighbours(p) if n in nums)
    return sum(adj.values())


def second_puzzle(symbols: Symbols, nums: Numbers) -> int:
    gears = [p for p, v in symbols.items() if v == "*"]
    adj = [set(nums[p] for p in neighbours(g) if p in nums) for g in gears]
    return sum(math.prod(n[1] for n in a) for a in adj if len(a) == 2)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(*data))
    print(second_puzzle(*data))
