"""Puzzles from https://adventofcode.com/2022/day/11"""

from copy import deepcopy
from functools import reduce
from math import lcm
from operator import mul
from pathlib import Path
from typing import Dict, List, Tuple


class Monkey:
    def __init__(self, items: List[int]):
        self.items: List[int] = items
        self.increase_data: Tuple[str, str] = (' ', ' ')
        self.decrease_worry_level = lambda x: x // 3
        self.test: int = 0
        self.where: Dict[bool, int] = {}
        self.inspected: int = 0

    def increase_worry_level(self, old: int) -> int:
        second_value = old
        if self.increase_data[1] != 'old':
            second_value = int(self.increase_data[1])
        if self.increase_data[0] == '+':
            return old + second_value
        else:
            return old * second_value

    def play_round(self, monkeys):
        for item in self.items:
            self.inspected += 1
            item = self.increase_worry_level(item)
            item = self.decrease_worry_level(item)
            monkeys[self.where[item % self.test == 0]].items.append(item)
        self.items = []


def read_data(filepath: Path) -> List[Monkey]:
    monkeys = []
    for line in open(filepath).read().splitlines():
        tokens = line.split(' ')
        if 'Starting items' in line:
            monkeys.append(Monkey([int(x.strip(',')) for x in tokens[4:]]))
        elif 'Operation' in line:
            monkeys[-1].increase_data = tokens[6], tokens[7]
        elif 'Test' in line:
            monkeys[-1].test = int(tokens[5])
        elif 'If true' in line:
            monkeys[-1].where = {True: int(tokens[9])}
        elif 'If false' in line:
            monkeys[-1].where[False] = int(tokens[9])
    return monkeys


def simulation(monkeys: List[Monkey], rounds: int) -> int:
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play_round(monkeys)
    return mul(*sorted(m.inspected for m in monkeys)[-2:])


def first_puzzle(monkeys: List[Monkey]) -> int:
    return simulation(monkeys, rounds=20)


def second_puzzle(monkeys: List[Monkey]) -> int:
    lcm_value = reduce(lcm, (m.test for m in monkeys))
    for monkey in monkeys:
        monkey.decrease_worry_level = lambda x: x % lcm_value
    return simulation(monkeys, rounds=10_000)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(deepcopy(data)))
    print(second_puzzle(deepcopy(data)))
