"""Puzzles from https://adventofcode.com/2023/day/1"""

from pathlib import Path
from typing import List, Iterable
from re import findall


def read_data(filepath: Path) -> List[str]:
    return open(filepath).read().splitlines()


def first_puzzle(lines: Iterable[str]) -> int:
    def value(line: str) -> int:
        digits = list(map(int, findall(r"\d", line)))
        return int(f"{digits[0]}{digits[-1]}")

    return sum(map(value, lines))


def second_puzzle(lines: Iterable[str]) -> int:
    def names_to_digits(line: str) -> str:
        return (
            line.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )

    return first_puzzle(map(names_to_digits, lines))


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
