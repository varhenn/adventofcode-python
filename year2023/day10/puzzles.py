#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/10"""
from pathlib import Path

Maze = tuple[complex, dict[complex, set[complex]]]


def read_data(filepath: Path) -> Maze:
    with open(filepath) as file:
        grid = {
            x + y * 1j: v
            for y, line in enumerate(file.read().split())
            for x, v in enumerate(line)
        }
        start = next(p for p, v in grid.items() if v == "S")
        deltas = {
            "|": [-1j, 1j],
            "-": [-1, 1],
            "L": [-1j, 1],
            "J": [-1j, -1],
            "7": [1j, -1],
            "F": [1j, 1],
            "S": [-1j, 1j, -1, 1],
        }
        area = {
            point: set(point + delta for delta in deltas.get(v, []))
            for point, v in grid.items()
            if v != "."
        }
        area[start] = set(n for n in area[start] if start in area.get(n, []))
        return start, area


def calc_loop(maze: Maze) -> set[complex]:
    start, area = maze
    loop = {start}
    todo = {start}
    while todo:
        nodes = area[todo.pop()]
        todo.update(nodes - loop)
        loop.update(nodes)
    return loop


def first_puzzle(maze: Maze) -> int:
    return len(calc_loop(maze)) // 2


def second_puzzle(maze: Maze) -> int:
    start, area = maze
    loop = calc_loop(maze)
    width = round(max(point.real for point in area.keys()))
    height = round(max(point.imag for point in area.keys()))
    tiles_inside = set()
    for x in range(width):
        pipes = 0
        for y in range(height):
            point = x + y * 1j
            if point in loop:
                if point + 1 in area[point]:  # one corner is enough
                    pipes += 1
            elif pipes % 2:
                tiles_inside.add(point)
    return len(tiles_inside)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
