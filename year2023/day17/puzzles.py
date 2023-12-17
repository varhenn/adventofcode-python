#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/17"""
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from heapq import heappop, heappush
from typing import Iterable

Grid = dict[complex, int]


@dataclass
class Node:
    p: complex  # point from the grid
    d: complex  # direction: -1j top, 1j bottom, 1 right, -1 left

    def neighbours(self, grid: Grid, moves: list[int]) -> Iterable[tuple[int, 'Node']]:
        for d in {1j * self.d, -1j * self.d}:
            for m in moves:
                if (p := self.p + m * d) in grid:
                    yield sum(grid[self.p + (x + 1) * d] for x in range(m)), Node(p, d)

    def __lt__(self, other):
        return True  # we need only sort by cost (complex don't have __lt__)

    def __hash__(self):
        return hash((self.p, self.d))  # needed for distances dict


def read_data(filepath: Path) -> Grid:
    with open(filepath) as file:
        rs = file.read().splitlines()
    return {x + y * 1j: int(c) for y, r in enumerate(rs) for x, c in enumerate(r)}


def first_puzzle(grid: Grid, moves=(1, 2, 3)) -> int:
    stop = [*grid][-1]
    ds = {1, -1, 1j, -1j}
    distances = defaultdict(lambda: float("inf"), {Node(0, d): 0 for d in ds})
    todo = [(0, Node(0j, 1 + 0j)), (0, Node(0j, 1j))]
    while todo:
        _, node = heappop(todo)
        if node.p == stop:
            return round(distances[node])
        for c, n in node.neighbours(grid, moves):
            if distances[node] + c < distances[n]:
                distances[n] = distances[node] + c
                heappush(todo, (distances[n], n))


def second_puzzle(grid: Grid) -> int:
    return first_puzzle(grid, moves=(4, 5, 6, 7, 8, 9, 10))


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
