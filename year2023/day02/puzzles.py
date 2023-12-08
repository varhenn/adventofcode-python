#!/usr/bin/env python3.11
"""Puzzles from https://adventofcode.com/2023/day/2"""
from pathlib import Path
from re import findall
from math import prod


def read_data(filepath: Path) -> dict[int, dict[str, int]]:
    return {
        int(idx): {
            color: max(int(n) for n in findall(f"(\d+) {color}", game))
            for color in ["red", "green", "blue"]
        }
        for idx, game in findall("Game (\d+): (.*)", open(filepath).read())
    }


def first_puzzle(games: dict[int, dict[str, int]]) -> int:
    return sum(
        idx
        for idx, game in games.items()
        if (game["red"] <= 12 and game["green"] <= 13 and game["blue"] <= 14)
    )


def second_puzzle(games: dict[int, dict[str, int]]) -> int:
    return sum(prod(game.values()) for game in games.values())


if __name__ == "__main__":
    data = read_data(Path(__file__).parent / "real.data")
    print(first_puzzle(data))
    print(second_puzzle(data))
