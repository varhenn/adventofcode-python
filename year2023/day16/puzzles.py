#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/16"""
from pathlib import Path


def read_data(filepath: Path) -> dict[complex, str]:
    with open(filepath) as file:
        rs = file.read().splitlines()
    return {x + 1j * y: c for y, r in enumerate(rs) for x, c in enumerate(r)}


def first_puzzle(
    grid: dict[complex, str], start: complex = 0, delta: complex = 1
) -> int:
    direction = {
        ".": lambda o: o,
        "|": lambda _: 1j,
        "-": lambda _: 1,
        "/": lambda o: -1j / o,
        "\\": lambda o: 1j / o,
    }
    todo = [(start, direction[grid[0]](delta))]
    done = set()
    while todo:
        p, d = todo.pop()
        while (p, d) not in done:
            done.add((p, d))
            p += d
            if p not in grid:
                break
            d = direction[grid[p]](d)
            if grid[p] in "|-":
                todo.append((p, -d))
    return len({p for p, _ in done})


def second_puzzle(grid: dict[complex, str]) -> int:
    return max(
        first_puzzle(grid, p, d)
        for p in grid
        for d in [1, -1, 1j, -1j]
        if p - d not in grid
    )


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
