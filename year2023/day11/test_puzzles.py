from pathlib import Path
from unittest import TestCase, main

from year2023.day11.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST_ANSWER = 374
FIRST_PUZZLE_REAL_ANSWER = 10276166
SECOND_PUZZLE_TEST_ANSWER = 82000210
SECOND_PUZZLE_REAL_ANSWER = 598693078798


class Year2023Day11Test(TestCase):
    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / "test.data")
        self.assertEqual(FIRST_PUZZLE_TEST_ANSWER, first_puzzle(data))

    def test_first_puzzle_real(self):
        data = read_data(Path(__file__).parent / "real.data")
        self.assertEqual(FIRST_PUZZLE_REAL_ANSWER, first_puzzle(data))

    def test_second_puzzle_test(self):
        data = read_data(Path(__file__).parent / "test.data")
        self.assertEqual(SECOND_PUZZLE_TEST_ANSWER, second_puzzle(data))

    def test_second_puzzle_real(self):
        data = read_data(Path(__file__).parent / "real.data")
        self.assertEqual(SECOND_PUZZLE_REAL_ANSWER, second_puzzle(data))


if __name__ == "__main__":
    main()
