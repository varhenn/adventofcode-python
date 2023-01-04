"""Puzzles from https://adventofcode.com/2022/day/21"""
from copy import deepcopy
from operator import add, sub, mul, truediv
from pathlib import Path
from re import findall
from typing import List, Union, Dict


def read_data(filepath: Path) -> Dict[str, Union[complex, List]]:
    operator = {'+': add, '-': sub, '*': mul, '/': truediv}
    raw = open(filepath).read()
    monkeys = {m: int(v) for m, v in findall(r"(\w+): (\d+)", raw)}
    monkeys |= {m: [l, operator[o], r] for m, l, o, r in
                findall(r"(\w+): (\w+) (.) (\w+)", raw)}
    return monkeys


def solve(key: str, monkeys: Dict[str, Union[complex, List]]) -> complex:
    if isinstance(job := monkeys[key], list):
        left, operator, right = job
        return operator(solve(left, monkeys), solve(right, monkeys))
    return job


def first_puzzle(data: Dict[str, Union[complex, List]]) -> int:
    return round(solve('root', data).real)


def second_puzzle(data: Dict[str, Union[complex, List]]) -> int:
    data['root'][1] = sub
    data['humn'] = -1j
    result = solve('root', data)
    return round(result.real / result.imag)


if __name__ == '__main__':
    real_data = read_data(Path(__file__).parent / 'test.data')
    print(first_puzzle(deepcopy(real_data)))
    print(second_puzzle(deepcopy(real_data)))
