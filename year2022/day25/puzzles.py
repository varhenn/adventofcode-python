"""Puzzles from https://adventofcode.com/2022/day/25"""

from pathlib import Path
from typing import List


def read_data(filepath: Path) -> List[str]:
    return open(filepath).read().splitlines()


def snafu_to_number(snafu: str) -> int:
    translate = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
    return sum(translate[ch] * 5 ** idx for idx, ch in enumerate(snafu[::-1]))


def number_to_snafu(number: int) -> str:
    reverse_snafu = ''
    while number:
        number, digit = divmod(number, 5)
        reverse_snafu += '012=-'[digit]
        number += digit > 2
    return reverse_snafu[::-1]


def first_puzzle(snafu_numbers: List[str]) -> str:
    return number_to_snafu(sum(map(snafu_to_number, snafu_numbers)))


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
