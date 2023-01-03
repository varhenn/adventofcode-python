"""Puzzles from https://adventofcode.com/2022/day/20"""

from pathlib import Path
from typing import List, Tuple


def read_data(filepath: Path) -> List[Tuple[int, int]]:
    # numbers at file may repeat, so must separate them (e.g. by enumerate)
    lines = open(filepath).read().splitlines()
    return [(idx, int(value)) for idx, value in enumerate(lines)]


def solve(data: List[Tuple[int, int]], repeat: int) -> int:
    tab = list(data)
    for _ in range(repeat):
        for val in data:
            idx = tab.index(val)
            tab.pop(idx)
            tab.insert((idx + val[1]) % len(tab), val)
    zero_idx = next(idx for idx, val in enumerate(tab) if val[1] == 0)
    return sum(tab[(zero_idx + x * 1_000) % len(tab)][1] for x in range(1, 4))


def first_puzzle(initial_numbers: List[Tuple[int, int]]) -> int:
    return solve(initial_numbers, repeat=1)


def second_puzzle(initial_numbers: List[Tuple[int, int]]) -> int:
    return solve([(i, 811589153 * v) for (i, v) in initial_numbers], repeat=10)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
