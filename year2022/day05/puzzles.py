"""Puzzles from https://adventofcode.com/2022/day/5"""
from collections import namedtuple, defaultdict
from copy import deepcopy
from pathlib import Path
from re import findall, finditer

Data = namedtuple('Data', 'stacks procedure')


def read_data(filepath: Path) -> Data:
    raw = open(filepath).read()
    stacks = defaultdict(list)
    for line in raw.splitlines():
        for m in finditer(r"[A-Z]", line):
            stacks[m.start(0) // 4 + 1] += [m.group(0)]
    moves = [tuple(map(int, m)) for m in
             findall(r"move (\d+) from (\d+) to (\d+)", raw)]
    return Data(stacks, moves)


def first_puzzle(data: Data, order: int = -1) -> str:
    stacks = deepcopy(data.stacks)
    for cnt, source, dest in data.procedure:
        stacks[dest] = stacks[source][:cnt][::order] + stacks[dest]
        stacks[source] = stacks[source][cnt:]
    return "".join(stacks[k][0] for k in sorted(stacks.keys()))


def second_puzzle(data: Data) -> str:
    return first_puzzle(data, order=1)


if __name__ == '__main__':
    real_data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(real_data))
    print(second_puzzle(real_data))
