"""Puzzles from https://adventofcode.com/2022/day/2"""
from pathlib import Path
from typing import List


def read_data(filepath: Path) -> List[str]:
    return open(filepath).read().splitlines()


def first_puzzle(rounds: List[str]) -> int:
    result = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
              'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
              'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3}
    return sum(result[r] for r in rounds)


def second_puzzle(rounds: List[str]) -> int:
    result = {'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
              'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
              'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6}
    return sum(result[r] for r in rounds)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
