import sys

import pytest


def load_input(fname: str) -> list[int]:
    """
    Load input data from the given file

    :param fname: input file name
    :return: list of integers
    """
    with open(fname) as fhandle:
        return [int(n) for n in fhandle.read().split()]


def two_numbers_to_2020(numbers: list[int]) -> int | None:
    """
    Get the product of two integers that adds to 2020

    :param numbers: list of integers
    :return: either an integer or None
    """
    n = len(numbers)
    for first_idx, first in enumerate(numbers):
        for second_idx in range(first_idx + 1, n):
            second = numbers[second_idx]
            if first + second == 2020:
                return first * second


def three_numbers_to_2020(numbers: list[int]) -> int | None:
    """
    Get the product of three integers that adds to 2020

    :param numbers: list of integers
    :return: either an integer or None
    """
    n = len(numbers)
    for first_idx, first in enumerate(numbers):
        for second_idx in range(first_idx + 1, n):
            second = numbers[second_idx]
            for third_idx in range(second_idx + 1, n):
                third = numbers[third_idx]
                if first + second + third == 2020:
                    return first * second * third



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
