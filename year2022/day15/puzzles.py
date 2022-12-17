"""Puzzles from https://adventofcode.com/2022/day/15"""
from collections import namedtuple
from pathlib import Path
from re import findall
from typing import List, Iterable, Optional

Point = namedtuple('Point', 'x y')
Report = namedtuple('Report', 'sensor beacon')
Range = namedtuple('Range', 'start end')  # start <= x < end


def read_data(filepath: Path) -> List[Report]:
    lines = open(filepath).read().splitlines()
    raw = (list(map(int, findall(r"-?\d+", line))) for line in lines)
    return [Report(Point(sx, sy), Point(bx, by)) for sx, sy, bx, by in raw]


def no_distress(reports: List[Report], row: int, limit: int) -> List[Range]:
    def to_range(report: Report, row: int):
        distance = sum(abs(s - b) for s, b in zip(report.sensor, report.beacon))
        delta = distance - abs(report.sensor.y - row)
        return Range(report.sensor.x - delta, report.sensor.x + delta + 1)

    prev = None
    ranges = []
    for act in sorted(to_range(rep, row) for rep in reports):
        if prev is None:
            prev = act
        elif act.start < prev.end:
            prev = Range(prev.start, max(prev.end, act.end))
        else:
            ranges.append(prev)
            prev = act
    ranges.append(prev)
    return ranges


def first_puzzle(reports: List[Report], row: int = 2_000_000) -> int:
    ranges = no_distress(reports, row, float('inf'))
    occupied = set(rep.beacon for rep in reports for ran in ranges
                   if rep.beacon.y == row
                   and ran.start <= rep.beacon.x < ran.end)
    return sum(ran.end - ran.start for ran in ranges) - len(occupied)


def second_puzzle(reports: List[Report], limit: int = 4_000_000) -> int:
    for y in range(limit):
        ranges = no_distress(reports, y, limit)
        x = 0
        for ran in ranges:
            if ran.start <= x < ran.end and x <= limit:
                x = ran.end
        if x <= limit:
            return x * 4_000_000 + y
    raise ValueError


if __name__ == '__main__':
    test_data = read_data(Path(__file__).parent / 'test.data')
    print(first_puzzle(test_data, row=10))
    print(second_puzzle(test_data, limit=20))

    real_data = read_data(Path(__file__).parent / 'real.data')
    print(first_puzzle(real_data))
    print(second_puzzle(real_data))
