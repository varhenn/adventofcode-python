"""Puzzles from https://adventofcode.com/2022/day/3"""
from pathlib import Path
from typing import List


def read_data(filepath: Path) -> List[str]:
    return open(filepath).read().splitlines()


def priority(letter: str) -> int:
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    return ord(letter) - ord('A') + 27


def first_puzzle(rucksacks: List[str]) -> int:
    def calc(line: str) -> int:
        mid = len(line) // 2
        in_both = set(line[:mid]) & set(line[mid:])
        return priority(in_both.pop())

    return sum(calc(r) for r in rucksacks)


def second_puzzle(rucksacks: List[str]) -> int:
    def calc(first: str, second: str, third) -> int:
        in_all = set(first) & set(second) & set(third)
        return priority(in_all.pop())

    return sum(calc(*rucksacks[x:x+3]) for x in range(0, len(rucksacks), 3))


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
