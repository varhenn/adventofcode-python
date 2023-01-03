"""Puzzles from https://adventofcode.com/2022/day/4"""
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
from re import findall
from typing import List, Tuple

Section = namedtuple('Section', 'first second')


@dataclass
class Range:
    start: int
    end: int

    def fully_contains(self, other) -> bool:
        return self.start <= other.start and other.end <= self.end

    def overlap(self, other) -> bool:
        return max(self.start, other.start) <= min(self.end, other.end)


def read_data(filepath: Path) -> List[Tuple[Range, Range]]:
    pattern = r"(\d+)-(\d+),(\d+)-(\d+)"
    sections = findall(pattern, open(filepath).read())
    return [(Range(int(a), int(b)), Range(int(c), int(d)))
            for a, b, c, d in sections]


def first_puzzle(sections: List[Tuple[Range, Range]]) -> int:
    return sum(x.fully_contains(y) or y.fully_contains(x) for x, y in sections)


def second_puzzle(sections: List[Tuple[Range, Range]]) -> int:
    return sum(x.overlap(y) for x, y in sections)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
