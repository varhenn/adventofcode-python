"""Puzzles from https://adventofcode.com/2022/day/14"""
from collections import namedtuple
from copy import deepcopy
from itertools import count
from pathlib import Path
from typing import Set

Point = namedtuple('Point', 'x y')


def read_data(filepath: Path) -> Set[Point]:
    tiles = set()
    for line in open(filepath).read().splitlines():
        path = [tuple(int(x) for x in t.split(',')) for t in line.split(' -> ')]
        for start, end in zip(path, path[1:]):
            delta = tuple((e > s) - (e < s) for s, e in zip(start, end))
            while start != end:
                tiles.add(Point(*start))
                start = tuple(x + y for x, y in zip(start, delta))
            tiles.add(Point(*end))
    return tiles


def first_puzzle(tiles: Set[Point]) -> int:
    abyss = max(p.y for p in tiles)
    for idx in count():
        prev, sand = Point(499, 0), Point(500, 0)
        if sand in tiles:
            return idx
        while prev != sand:
            prev = sand
            for x_step in [0, -1, 1]:
                if (moved := Point(sand.x + x_step, sand.y + 1)) not in tiles:
                    sand = moved
                    break
            if sand.y >= abyss:
                return idx
        tiles.add(sand)


def second_puzzle(tiles: Set[Point]) -> int:
    y = max(p.y for p in tiles) + 2
    for x in range(500 - y - 3, 500 + y + 3):
        tiles.add(Point(x, y))
    return first_puzzle(tiles)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(deepcopy(data)))
    print(second_puzzle(deepcopy(data)))
