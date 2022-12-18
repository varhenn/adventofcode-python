"""Puzzles from https://adventofcode.com/2022/day/18"""

from collections import deque
from pathlib import Path
from typing import Set, Tuple


def read_data(filepath: Path) -> Set[Tuple[int, int, int]]:
    lines = open(filepath).read().splitlines()
    return {tuple(map(int, line.split(','))) for line in lines}


def neighbours(x: int, y: int, z: int) -> Set[Tuple[int, int, int]]:
    return {(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z),
            (x, y, z - 1), (x, y, z + 1)}


def first_puzzle(cubes: Set[Tuple[int, int, int]]) -> int:
    return sum(n not in cubes for c in cubes for n in neighbours(*c))


def second_puzzle(cubes: Set[Tuple[int, int, int]]) -> int:
    air_min_position = min(min(*c) for c in cubes) - 1
    air_max_position = max(max(*c) for c in cubes) + 1

    def is_in_area(cube: Tuple[int, int, int]) -> bool:
        return all(air_min_position <= p <= air_max_position for p in cube)

    first_air_cube = (air_min_position, air_min_position, air_min_position)
    air_cubes = {first_air_cube}
    todo = deque([first_air_cube])
    while todo:
        air = todo.pop()
        for n in neighbours(*air) - cubes - air_cubes:
            if is_in_area(n):
                air_cubes.add(n)
                todo.appendleft(n)
    return sum(n in air_cubes for c in cubes for n in neighbours(*c))


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
