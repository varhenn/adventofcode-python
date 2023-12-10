from pathlib import Path
from unittest import TestCase, main

from year2023.day10.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST_ANSWER = 8
FIRST_PUZZLE_REAL_ANSWER = 7063
SECOND_PUZZLE_TEST2_ANSWER = 8
SECOND_PUZZLE_REAL_ANSWER = 589


class Year2023Day10Test(TestCase):
    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / "test.data")
        self.assertEqual(FIRST_PUZZLE_TEST_ANSWER, first_puzzle(data))

    def test_first_puzzle_real(self):
        data = read_data(Path(__file__).parent / "real.data")
        self.assertEqual(FIRST_PUZZLE_REAL_ANSWER, first_puzzle(data))

    def test_second_puzzle_test(self):
        data = read_data(Path(__file__).parent / "test2.data")
        self.assertEqual(SECOND_PUZZLE_TEST2_ANSWER, second_puzzle(data))

    def test_second_puzzle_real(self):
        data = read_data(Path(__file__).parent / "real.data")
        self.assertEqual(SECOND_PUZZLE_REAL_ANSWER, second_puzzle(data))


if __name__ == "__main__":
    main()
