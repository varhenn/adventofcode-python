from pathlib import Path
from unittest import TestCase, main

from year2022.day25.puzzles import read_data, first_puzzle, snafu_to_number, \
    number_to_snafu

FIRST_PUZZLE_TEST_ANSWER = '2=-1=0'
FIRST_PUZZLE_REAL_ANSWER = '2-212-2---=00-1--102'


class Year2022Day25Test(TestCase):
    def setUp(self):
        self.snafu_number_list = [
            ('1', 1),
            ('2', 2),
            ('1=', 3),
            ('1-', 4),
            ('10', 5),
            ('11', 6),
            ('12', 7),
            ('2=', 8),
            ('2-', 9),
            ('20', 10),
            ('1=0', 15),
            ('1-0', 20),
            ('1=11-2', 2022),
            ('1-0---0', 12345),
            ('1121-1110-1=0', 314159265),
            ('1=-0-2', 1747),
            ('12111', 906),
            ('2=0=', 198),
            ('21', 11),
            ('2=01', 201),
            ('111', 31),
            ('20012', 1257),
            ('112', 32),
            ('1=-1=', 353),
            ('1-12', 107),
            ('12', 7),
            ('1=', 3),
            ('122', 37),
        ]

    def test_snafu_to_number(self):
        for snafu, decimal in self.snafu_number_list:
            self.assertEqual(decimal, snafu_to_number(snafu))

    def test_number_to_snafu(self):
        for snafu, decimal in self.snafu_number_list:
            self.assertEqual(snafu, number_to_snafu(decimal))

    def test_first_puzzle_test(self):
        data = read_data(Path(__file__).parent / 'test.data')
        self.assertEqual(FIRST_PUZZLE_TEST_ANSWER, first_puzzle(data))

    def test_first_puzzle_real(self):
        data = read_data(Path(__file__).parent / 'real.data')
        self.assertEqual(FIRST_PUZZLE_REAL_ANSWER, first_puzzle(data))


if __name__ == '__main__':
    main()
