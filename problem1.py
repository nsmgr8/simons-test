import sys

import pytest


def load_input(fname):
    with open(fname) as fhandle:
        return [int(n) for n in fhandle.read().split()]


def two_numbers_to_2020(numbers):
    ...


def three_numbers_to_2020(numbers):
    ...



def main(input_file='input/input1.txt'):
    numbers = load_input(input_file)
    print(two_numbers_to_2020(numbers))
    print(three_numbers_to_2020(numbers))


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])


@pytest.fixture
def input_data():
    return [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]


def test_two_numbers(input_data):
    assert two_numbers_to_2020(input_data) == 514579


def test_three_numbers(input_data):
    assert three_numbers_to_2020(input_data) == 241861950
