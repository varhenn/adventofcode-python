"""Puzzles from https://adventofcode.com/2022/day/8"""

from itertools import takewhile
from math import prod
from pathlib import Path
from typing import Dict, Tuple, Iterable, List

Point = Tuple[int, int]
Grid = Dict[Point, int]
Lines = Tuple[Iterable[int], Iterable[int], Iterable[int], Iterable[int]]


def read_data(filepath: Path) -> Grid:
    return {(x, y): int(h)
            for y, line in enumerate(open(filepath).read().splitlines())
            for x, h in enumerate(line)}


def heights_from(grid: Grid, tree: Point, delta: Point) -> Iterable[int]:
    idx = tree
    while (idx := (idx[0] + delta[0], idx[1] + delta[1])) in grid:
        yield grid[idx]


def directions(grid: Grid, tree: Point) -> Lines:
    left = heights_from(grid, tree, (1, 0))
    right = heights_from(grid, tree, (-1, 0))
    down = heights_from(grid, tree, (0, 1))
    top = heights_from(grid, tree, (0, -1))
    return left, right, down, top


def first_puzzle(forest: Dict[Point, int]) -> int:
    def visible(height: int, lines: Lines) -> bool:
        return any(height > max(line, default=-1) for line in lines)

    return sum(visible(h, directions(forest, p)) for p, h in forest.items())


def second_puzzle(forest: Dict[Point, int]) -> int:
    def score(height: int, lines: Lines) -> int:
        def visible(height: int, line: List[int]) -> int:
            cnt = sum(1 for _ in takewhile(lambda x: x < height, line))
            return cnt < len(line) and cnt + 1 or cnt

        return prod(visible(height, list(line)) for line in lines)

    return max(score(h, directions(forest, p)) for p, h in forest.items())


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
