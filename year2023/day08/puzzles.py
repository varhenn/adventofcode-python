#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/8"""
from itertools import cycle
from math import lcm
from pathlib import Path
from re import finditer

Network = tuple[str, dict[str, tuple[str, str]]]


def read_data(filepath: Path) -> Network:
    with open(filepath) as file:
        instructions = file.readline().rstrip()
        edges = finditer(r"(\w+) = .(\w+), (\w+).", file.read())
        nodes = {e[1]: (e[2], e[3]) for e in edges}
        return instructions, nodes


def steps_to_first_end(node: str, network: Network, is_last_z: bool) -> int:
    instructions, nodes = network
    for cnt, direction in enumerate(cycle(instructions), 1):
        node = nodes[node][direction == "R"]
        if node == "ZZZ" or is_last_z and node[-1] == "Z":
            return cnt


def first_puzzle(network: Network) -> int:
    return steps_to_first_end("AAA", network, is_last_z=False)


def second_puzzle(network: tuple[str, dict[str, tuple[str, str]]]) -> int:
    starts = (n for n in network[1].keys() if n[-1] == "A")
    endings = [steps_to_first_end(n, network, is_last_z=True) for n in starts]
    return lcm(*endings)  # NOTE: data don't require Chinese remainder theorem


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
