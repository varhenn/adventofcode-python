from pathlib import Path
from unittest import TestCase, main

from year2022.day06.puzzles import read_data, first_puzzle, second_puzzle

FIRST_PUZZLE_TEST_ANSWER = 7
FIRST_PUZZLE_REAL_ANSWER = 1909
SECOND_PUZZLE_TEST_ANSWER = 19
SECOND_PUZZLE_REAL_ANSWER = 3380


class Year2022Day18Test(TestCase):
    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / 'test.data')
        self.assertEqual(FIRST_PUZZLE_TEST_ANSWER, first_puzzle(data))
        self.assertEqual(5, first_puzzle('bvwbjplbgvbhsrlpgdmjqwftvncz'))
        self.assertEqual(6, first_puzzle('nppdvjthqldpwncqszvftbrmjlhg'))
        self.assertEqual(10, first_puzzle('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
        self.assertEqual(11, first_puzzle('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))

    def test_first_puzzle_real(self):
        data = read_data(Path(__file__).parent / 'real.data')
        self.assertEqual(FIRST_PUZZLE_REAL_ANSWER, first_puzzle(data))

    def test_second_puzzle_test(self):
        data = read_data(Path(__file__).parent / 'test.data')
        self.assertEqual(SECOND_PUZZLE_TEST_ANSWER, second_puzzle(data))

    def test_second_puzzle_real(self):
        data = read_data(Path(__file__).parent / 'real.data')
        self.assertEqual(SECOND_PUZZLE_REAL_ANSWER, second_puzzle(data))
        self.assertEqual(23, second_puzzle('bvwbjplbgvbhsrlpgdmjqwftvncz'))
        self.assertEqual(23, second_puzzle('nppdvjthqldpwncqszvftbrmjlhg'))
        self.assertEqual(29, second_puzzle('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
        self.assertEqual(26, second_puzzle('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))


if __name__ == '__main__':
    main()
