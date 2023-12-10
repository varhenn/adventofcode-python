#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/9"""
from pathlib import Path


def read_data(filepath: Path) -> list[list[int]]:
    with open(filepath) as file:
        return [list(map(int, line.split())) for line in file.readlines()]


def calc_history(nums: list[int]) -> int:
    value = nums[-1]
    while any(nums):
        nums = [a - b for a, b in zip(nums[1:], nums[:-1])]
        value += nums[-1]
    return value


def first_puzzle(histories: list[list[int]]) -> int:
    return sum(calc_history(h) for h in histories)


def second_puzzle(histories: list[list[int]]) -> int:
    return sum(calc_history(h[::-1]) for h in histories)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
