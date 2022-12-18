"""Puzzles from https://adventofcode.com/2022/day/10"""

from collections import namedtuple
from pathlib import Path
from typing import Dict

Point = namedtuple('Point', 'x y')


def read_data(filepath: Path) -> Dict[int, int]:
    values, cycle, value = {1: 1}, 1, 1
    for line in open(filepath).read().splitlines():
        cycle += 1
        values[cycle] = value
        if len(tokens := line.split(' ')) == 2:
            cycle += 1
            value += int(tokens[1])
            values[cycle] = value
    return values


def first_puzzle(values: Dict[int, int]) -> int:
    return sum(cycle * values[cycle] for cycle in range(20, 221, 40))


def second_puzzle(values: Dict[int, int]) -> str:
    draw = {True: '#', False: '.'}
    lines = []
    for c in range(1, 241, 40):
        lines.append("".join(draw[values[x] <= x % 40 < values[x] + 3]
                             for x in range(c, c + 40)))
    return "\n".join(lines)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
