from pathlib import Path
from unittest import TestCase, main

from year2022.day10.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST_ANSWER = 13140
FIRST_PUZZLE_REAL_ANSWER = 14060
SECOND_PUZZLE_TEST_ANSWER = \
    '##..##..##..##..##..##..##..##..##..##..\n' \
    '###...###...###...###...###...###...###.\n' \
    '####....####....####....####....####....\n' \
    '#####.....#####.....#####.....#####.....\n' \
    '######......######......######......###.\n' \
    '#######.......#######.......#######.....'
SECOND_PUZZLE_REAL_ANSWER = \
    '###...##..###..#..#.####.#..#.####...###\n' \
    '#..#.#..#.#..#.#.#..#....#.#..#.......##\n' \
    '#..#.#..#.#..#.##...###..##...###.....##\n' \
    '###..####.###..#.#..#....#.#..#.......#.\n' \
    '#....#..#.#....#.#..#....#.#..#....#..#.\n' \
    '#....#..#.#....#..#.#....#..#.####..##..'


class Year2022Day10Test(TestCase):
    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / 'test.data')
        self.assertEqual(FIRST_PUZZLE_TEST_ANSWER, first_puzzle(data))

    def test_first_puzzle_real(self):
        data = read_data(Path(__file__).parent / 'real.data')
        self.assertEqual(FIRST_PUZZLE_REAL_ANSWER, first_puzzle(data))

    def test_second_puzzle_test(self):
        data = read_data(Path(__file__).parent / 'test.data')
        self.assertEqual(SECOND_PUZZLE_TEST_ANSWER, second_puzzle(data))

    def test_second_puzzle_real(self):
        data = read_data(Path(__file__).parent / 'real.data')
        self.assertEqual(SECOND_PUZZLE_REAL_ANSWER, second_puzzle(data))


if __name__ == '__main__':
    main()
