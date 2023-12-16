#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/15"""
from collections import defaultdict
from functools import reduce
from pathlib import Path
from re import match


def read_data(filepath: Path) -> list[str]:
    with open(filepath) as file:
        return file.read().strip("\n").split(",")


def calc_hash(step: str) -> int:
    return reduce(lambda v, c: (v + ord(c)) * 17 % 256, step, 0)


def first_puzzle(steps: list[str]) -> int:
    return sum(map(calc_hash, steps))


def second_puzzle(steps: list[str]) -> int:
    boxes = defaultdict(dict)
    for step in steps:
        label, op, length = match(r"(\w+)([=-])(\d*)", step).groups()
        if op == "=":
            boxes[calc_hash(label)][label] = int(length)
        else:
            boxes[calc_hash(label)].pop(label, None)
    return sum(
        (box + 1) * slot * focal
        for box, lens in boxes.items()
        for slot, focal in enumerate(lens.values(), 1)
    )


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
