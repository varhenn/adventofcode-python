from pathlib import Path
from unittest import TestCase, main

from year2022.day20.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST_ANSWER = 3
FIRST_PUZZLE_REAL_ANSWER = 6640
SECOND_PUZZLE_TEST_ANSWER = 1623178306
SECOND_PUZZLE_REAL_ANSWER = 11893839037215


class Year2022Day20Test(TestCase):
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
