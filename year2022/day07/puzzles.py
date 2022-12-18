"""Puzzles from https://adventofcode.com/2022/day/7"""

from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import Dict


def read_data(filepath: Path) -> Dict[Path, int]:
    totals = defaultdict(int)
    pwd = Path('/')
    for line in open(filepath).read().splitlines():
        tokens = line.split(' ')
        if line.startswith('$ cd /'):
            pwd = Path('/')
        elif line.startswith('$ cd ..'):
            pwd = pwd.parent
        elif line.startswith('$ cd'):
            pwd = pwd / tokens[2]
        elif tokens[0].isnumeric():
            filesize = int(tokens[0])
            for act in chain([pwd], pwd.parents):
                totals[act] += filesize
    return totals


def first_puzzle(totals: Dict[Path, int]) -> int:
    return sum(x for x in totals.values() if x <= 100_000)


def second_puzzle(totals: Dict[Path, int]) -> int:
    unused = 70_000_000 - totals[Path('/')]
    return min(x for x in totals.values() if unused + x >= 30_000_000)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
