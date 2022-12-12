"""Puzzles from https://adventofcode.com/2022/day/12"""
from collections import namedtuple, deque
from pathlib import Path
from typing import Dict, Iterable

Point = namedtuple('Point', 'x y')
Heightmap = namedtuple('Data', 'start end area')


def read_data(filepath: Path) -> Heightmap:
    start, end, area = None, None, {}
    for y, line in enumerate(open(filepath).read().splitlines()):
        for x, elevation in enumerate(line):
            if elevation == 'S':
                start = Point(x, y)
                area[Point(x, y)] = 0
            elif elevation == 'E':
                end = Point(x, y)
                area[Point(x, y)] = int(ord('z') - ord('a'))
            else:
                area[Point(x, y)] = int(ord(elevation) - ord('a'))
    return Heightmap(start, end, area)


def neighbours(point: Point) -> Iterable[Point]:
    for x_step, y_step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        yield Point(point.x + x_step, point.y + y_step)


def distances_from_end(end: Point, area: Dict[Point, int]) -> Dict[Point, int]:
    todo, visited = deque([end]), {end: 0}
    while todo:
        act = todo.popleft()
        for ngh in neighbours(act):
            if ngh in area and ngh not in visited and area[act] - area[ngh] < 2:
                todo.append(ngh)
                visited[ngh] = visited[act] + 1
    return visited


def first_puzzle(heightmap: Heightmap) -> int:
    return distances_from_end(heightmap.end, heightmap.area)[heightmap.start]


def second_puzzle(heightmap: Heightmap) -> int:
    distances = distances_from_end(heightmap.end, heightmap.area)
    return min(d for p, d in distances.items() if heightmap.area[p] == 0)


if __name__ == '__main__':
    data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(data))
    print(second_puzzle(data))
