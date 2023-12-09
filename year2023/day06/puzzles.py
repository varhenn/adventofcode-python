#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/6"""
from math import floor, ceil, prod
from pathlib import Path
from re import findall


def read_data(filepath: Path) -> tuple[list[str], list[str]]:
    with open(filepath) as file:
        return tuple(findall(r"\d+", line) for line in file.readlines())


def _solve(time: int, distance: int) -> int:
    def quadratic_equation(a: int, b: int, c: int) -> tuple[float, float]:
        delta = b**2 - 4 * a * c
        if delta >= 0:
            x1 = (-b + delta**0.5) / (2 * a)
            x2 = (-b - delta**0.5) / (2 * a)
            return x1, x2

    # x(time - x) >= distance
    results = quadratic_equation(-1, time, -distance)
    return ceil(max(*results)) - floor(min(*results)) - 1


def first_puzzle(document: tuple[list[str], list[str]]) -> int:
    races = [(int(t), int(d)) for t, d in zip(*document)]
    return prod(_solve(t, d) for t, d in races)


def second_puzzle(document: tuple[list[str], list[str]]) -> int:
    return _solve(int("".join(document[0])), int("".join(document[1])))


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
