#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/14"""
from itertools import count
from pathlib import Path
from typing import Iterable


class Grid:
    def __init__(self, grid: dict[complex, str]):
        # width == height here
        self.size = round(max(p.real for p in grid.keys())) + 1
        self.rounded = {p for p, v in grid.items() if v == "O"}
        self.blocked = {p for p, v in grid.items() if v == "#"}
        self.points = set(grid.keys())

    def move(self, directions: Iterable[complex]) -> None:
        for d in directions:
            while True:
                empties = self.points - self.blocked - self.rounded
                rounded = {r + d if r + d in empties else r for r in self.rounded}
                if rounded == self.rounded:
                    break
                self.rounded = rounded

    def total_load(self) -> int:
        return sum(round(self.size - p.imag) for p in self.rounded)


def read_data(filepath: Path) -> Grid:
    with open(filepath) as file:
        rs = file.read().splitlines()
    return Grid({x + 1j * y: c for y, r in enumerate(rs) for x, c in enumerate(r)})


def first_puzzle(grid: Grid) -> int:
    grid.move([-1j])
    return grid.total_load()


def second_puzzle(grid: Grid) -> int:
    seen = []
    for idx in count():
        grid.move([-1j, -1, 1j, 1])
        if grid.rounded in seen:
            start_idx = seen.index(grid.rounded)
            break
        seen.append(grid.rounded)
    final_idx = (1_000_000_000 - idx) % (start_idx - idx) + idx - 1
    grid.rounded = seen[final_idx]
    return grid.total_load()


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
