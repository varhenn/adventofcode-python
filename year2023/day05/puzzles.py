#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/5"""
from functools import reduce
from pathlib import Path
from re import findall
from collections import deque

Seeds = list[int]
Range = tuple[int, int]  # seed_beg, seed_end
Maps = list[tuple[int, int, int]]  # out_beg, inp_beg, _inp_end_


def read_data(filepath: Path) -> tuple[Seeds, list[Maps]]:
    # no parse "<source>-to-<destination> map:" lines, file has good order
    def fix(line: str) -> tuple[int, int, int]:
        # out_beg inp_beg inp_len --> out_beg inp_beg inp_end
        a, b, c = map(int, line.split())
        return a, b, b + c

    with open(filepath) as file:
        raw_seeds, *raw_maps = file.read().split("\n\n")
        seeds = [int(s) for s in findall(r"\d+", raw_seeds)]
        l_maps = [[fix(line) for line in m.split("\n")[1:]] for m in raw_maps]
        return seeds, l_maps


def _solve(seed_ranges: list[Range], maps: list[Maps]) -> int:
    def do_category(seed_ranges: list[Range], ranges: Maps):
        todo = deque(seed_ranges)
        done = deque()
        while todo:
            c_beg, c_end = todo.popleft()
            for s_beg, d_beg, d_end in ranges:
                if c_end <= d_beg or d_end <= c_beg:
                    continue
                if c_beg < d_beg:
                    todo.append((c_beg, d_beg))
                if c_end > d_end:
                    todo.append((d_end, c_end))
                s = s_beg + max(c_beg, d_beg) - d_beg
                l = min(c_end, d_end) - max(c_beg, d_beg)
                done.append((s, s + l))
                break
            else:
                done.append((c_beg, c_end))
        return done  # NOTE: sort and concatenate is need

    return min(sr[0] for sr in reduce(do_category, maps, seed_ranges))


def first_puzzle(almanac: tuple[Seeds, list[Maps]]) -> int:
    seeds, maps = almanac
    seed_ranges = [(s, s + 1) for s in seeds]
    return _solve(seed_ranges, maps)


def second_puzzle(almanac: tuple[Seeds, list[Maps]]) -> int:
    seeds, maps = almanac
    seed_ranges = [(s, s + l) for s, l in zip(seeds[::2], seeds[1::2])]
    return _solve(seed_ranges, maps)


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
