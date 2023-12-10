from pathlib import Path
from unittest import TestCase, main

from year2023.day08.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST0_ANSWER = 2
FIRST_PUZZLE_TEST1_ANSWER = 6
FIRST_PUZZLE_REAL_ANSWER = 15871
SECOND_PUZZLE_TEST2_ANSWER = 6
SECOND_PUZZLE_REAL_ANSWER = 11283670395017


class Year2023Day08Test(TestCase):
    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / "test0.data")
        self.assertEqual(FIRST_PUZZLE_TEST0_ANSWER, first_puzzle(data))

    def test_first_puzzle_test_second(self):
        data = read_data(Path(__file__).parent / "test1.data")
        self.assertEqual(FIRST_PUZZLE_TEST1_ANSWER, first_puzzle(data))

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
