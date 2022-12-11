"""Puzzles from https://adventofcode.com/2022/day/1"""

from pathlib import Path
from typing import List


def read_data(filepath: Path) -> List[int]:
    elves = [0]
    for line in open(filepath).read().splitlines():
        if line:
            elves[-1] += int(line)
        else:
            elves.append(0)
    return elves


def first_puzzle(elves: List[int]) -> int:
    return max(elves)


def second_puzzle(elves: List[int]) -> int:
    return sum(sorted(elves)[-3:])


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
