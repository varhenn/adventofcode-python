#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/19"""
from math import prod
from pathlib import Path
from re import findall
from operator import lt, gt

Rule = tuple[str, str, str, str]
Part = dict[str, int]
PartRange = dict[str, tuple[int, int]]
Workflows = dict[str, list[Rule]]


def read_data(filepath: Path) -> tuple[Workflows, list[Part]]:
    with open(filepath) as file:
        workflows, parts = file.read().split("\n\n")
    return (
        {
            n: findall(r"(\w)([<>])(\d+):(\w+)", rs) + [("", "", "", rs.split(",")[-1])]
            for n, rs in findall(r"(\w+)\{(.*)}", workflows)
        },
        [
            {c: int(v) for c, v in findall(r"(\w)=(\d+)", part)}
            for part in parts.split("\n")
        ],
    )


def first_puzzle(system: tuple[Workflows, list[Part]]) -> int:
    def calc(part: Part, name: str) -> int:
        while name not in {"A", "R"}:
            for c, o, v, n in workflows[name]:
                if o == "" or {"<": lt, ">": gt}[o](part[c], int(v)):
                    name = n
                    break
        return sum(part.values()) if name == "A" else 0

    workflows, parts = system
    return sum(calc(part, "in") for part in parts)


def second_puzzle(system: tuple[Workflows, list[Part]]) -> int:
    def calc(part_range: PartRange, name: str) -> int:
        if name == "A":
            return prod(e - b for b, e in part_range.values())
        if name == "R":
            return 0
        result = 0
        for c, o, v, n in workflows[name]:
            if o == "":
                return result + calc(part_range, n)
            b, e, v = *part_range[c], int(v)
            if o == "<" and b < v:
                result += calc({**part_range, c: (b, v)}, n)
                part_range = {**part_range, c: (v, e)}
            if o == ">" and v < e - 1:
                result += calc({**part_range, c: (v + 1, e)}, n)
                part_range = {**part_range, c: (b, v + 1)}
        return result

    workflows, _ = system
    return calc({c: (1, 4_001) for c in "xmas"}, "in")


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "test.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
