"""Puzzles from https://adventofcode.com/2022/day/9"""

from collections import namedtuple
from pathlib import Path
from typing import Tuple, Iterable, List

Point = namedtuple('Point', 'x y')


def read_data(filepath: Path) -> Iterable[Tuple[Point, int]]:
    direction = {'R': Point(1, 0), 'L': Point(-1, 0), 'U': Point(0, 1),
                 'D': Point(0, -1)}
    for line in open(filepath).read().splitlines():
        tokens = line.split(' ')
        yield direction[tokens[0]], int(tokens[1])


def knot_keeping_up(moved: Point, knot: Point) -> Point:
    delta = Point(moved.x - knot.x, moved.y - knot.y)
    if abs(delta.x) <= 1 and abs(delta.y) <= 1:
        return knot
    clamp = {-2: -1, -1: -1, 0: 0, 1: 1, 2: 1}
    return Point(knot.x + clamp[delta.x], knot.y + clamp[delta.y])


def step(snake: List[Point], direction: Point) -> List[Point]:
    moved = [Point(snake[0].x + direction.x, snake[0].y + direction.y)]
    for prev_idx, part in enumerate(snake[1:]):
        moved.append(knot_keeping_up(moved[-1], part))
    return moved


def simulation(snake: List[Point], commands: Iterable[Tuple[Point, int]]):
    visited = {snake[-1]}
    for direction, steps in commands:
        for _ in range(steps):
            snake = step(snake, direction)
            visited.add(snake[-1])
    return len(visited)


def first_puzzle(commands: Iterable[Tuple[Point, int]]) -> int:
    return simulation([Point(0, 0), Point(0, 0)], commands)


def second_puzzle(commands: Iterable[Point[str, int]]) -> int:
    return simulation([Point(0, 0) for _ in range(10)], commands)


if __name__ == '__main__':
    data = list(read_data(Path(__file__).parent / 'real.data'))
    print(first_puzzle(data))
    print(second_puzzle(data))
