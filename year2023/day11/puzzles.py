#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/11"""
from pathlib import Path
from itertools import accumulate, combinations

Data = tuple[list[tuple[int, int]], list[int], list[int]]


def read_data(filepath: Path) -> Data:
    with open(filepath) as file:
        lines = file.read().splitlines()
    galaxies, rows, cols = [], [1] * len(lines), [1] * len(lines[0])
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v == "#":
                galaxies.append((x, y))
                cols[x], rows[y] = 0, 0
    return galaxies, list(accumulate(rows)), list(accumulate(cols))


def first_puzzle(universe: Data, n: int = 2) -> int:
    galaxies, dy, dx = universe
    expanded = [(x + (n - 1) * dx[x], y + (n - 1) * dy[y]) for x, y in galaxies]
    pairs = combinations(expanded, 2)
    return sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in pairs)


def second_puzzle(universe: Data) -> int:
    return first_puzzle(universe, n=1_000_000)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
