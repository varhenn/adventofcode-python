#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/18"""
from itertools import accumulate, pairwise
from pathlib import Path
from re import findall


def read_data(filepath: Path) -> list[tuple[str, str, str]]:
    with open(filepath) as file:
        return findall(r"(\w) (\d+) .#([0-9a-z]{6}).", file.read())


def solve(plan: list[tuple[complex, int]]) -> int:
    def triangle_formula(a: complex, b: complex) -> float:
        return (a.real * b.imag - a.imag * b.real) / 2

    boundary = sum(steps for _, steps in plan)
    polygon = accumulate(d * s for d, s in plan)
    shoelace = abs(sum(triangle_formula(a, b) for a, b in pairwise(polygon)))
    return round(shoelace + boundary // 2 + 1)  # Pick's theorem


def first_puzzle(raw_plan: list[tuple[str, str, str]]) -> int:
    dirs = {"R": 1 + 0j, "L": -1 + 0j, "U": -1j, "D": 1j}
    return solve([(dirs[d], int(s)) for d, s, _ in raw_plan])


def second_puzzle(raw_plan: list[tuple[str, str, str]]) -> int:
    dirs = {"0": 1 + 0j, "2": -1 + 0j, "3": -1j, "1": 1j}
    return solve([(dirs[c[5]], int(c[0:5], 16)) for _, _, c in raw_plan])


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
