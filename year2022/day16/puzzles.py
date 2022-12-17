"""Puzzles from https://adventofcode.com/2022/day/16"""

from collections import namedtuple, defaultdict, deque
from itertools import product, repeat
from math import inf
from pathlib import Path
from re import findall
from typing import Dict, Iterable, Set, Tuple

Data = namedtuple('Data', 'valves rates edges')
Distances = Dict[str, Dict[str, int]]
Solution = Tuple[int, Set[str]]


def read_data(filepath: Path) -> Data:
    pattern = r"Valve ([A-Z]{2}) has flow rate=(\d+);.+to valves? (.+)"
    lines = findall(pattern, open(filepath).read())
    valves = set(v for v, _, _ in lines)
    rates = {v: int(r) for v, r, _ in lines}
    edges = set((v, t) for v, _, tunnels in lines for t in tunnels.split(', '))
    return Data(valves, rates, edges)


def solutions(data: Data, start: str, time: int) -> Iterable[Solution]:
    def calc_shortest_distances(data: Data) -> Distances:
        # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
        paths = defaultdict(lambda: defaultdict(lambda: inf))
        for a in data.valves:
            paths[a][a] = 0
        for a, b in data.edges:
            paths[a][b] = 1
        for b, a, c in product(*repeat(data.valves, 3)):
            paths[a][c] = min(paths[a][c], paths[a][b] + paths[b][c])
        return paths

    distances = calc_shortest_distances(data)
    todo = deque([(start, time, 0, set([]))])
    while todo:
        last, time, score, visited = todo.pop()
        for valve in (data.valves - visited):
            if data.rates[valve] == 0:
                continue
            if (left := time - distances[last][valve] - 1) < 2:
                continue
            next_score = score + left * data.rates[valve]
            next_visited = visited | {valve}
            todo.appendleft((valve, left, next_score, next_visited))
        yield score, visited


def first_puzzle(data: Data) -> int:
    return max(score for score, _ in solutions(data, start='AA', time=30))


def second_puzzle(data: Data) -> int:
    scores = defaultdict(int)
    for score, visited in solutions(data, start='AA', time=26):
        key = frozenset(visited)
        scores[key] = max(score, scores[key])
    return max(sa + sb
               for (va, sa), (vb, sb) in product(scores.items(), scores.items())
               if len(va & vb) == 0)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'test.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
