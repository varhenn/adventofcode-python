"""Puzzles from https://adventofcode.com/2022/day/13"""
from functools import cmp_to_key
from math import prod
from pathlib import Path
from typing import List, Any


def read_data(filepath: Path) -> List[Any]:
    return [eval(x) for x in open(filepath).read().splitlines() if x]


def cmp_right_order(left: int, right: int) -> int:
    return (left > right) - (left < right)


def right_order(left: Any, right: Any) -> int:
    if type(left) == int and type(right) == int:
        return cmp_right_order(left, right)
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for left_child, right_child in zip(left, right):
        result = right_order(left_child, right_child)
        if result != 0:
            return result
    return cmp_right_order(len(left), len(right))


def first_puzzle(packets: List[Any]) -> int:
    pairs = zip(packets[::2], packets[1::2])
    return sum(idx + 1 for idx, p in enumerate(pairs) if right_order(*p) == -1)


def second_puzzle(packets: List[Any]) -> int:
    dividers = [[[2]], [[6]]]
    sorted_all_packets = sorted(packets + dividers, key=cmp_to_key(right_order))
    return prod(idx + 1
                for idx, value in enumerate(sorted_all_packets)
                if value == dividers[0] or value == dividers[1])


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
