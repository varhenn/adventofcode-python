"""Puzzles from https://adventofcode.com/2022/day/6"""

from pathlib import Path
from typing import Optional


def read_data(filepath: Path) -> str:
    return open(filepath).read()


def first_puzzle(signal: str, marker: int = 4) -> Optional[int]:
    for idx in range(len(signal) - marker + 1):
        if len(set(signal[idx:idx + marker])) == marker:
            return idx + marker


def second_puzzle(signal: str) -> Optional[int]:
    return first_puzzle(signal, marker=14)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
