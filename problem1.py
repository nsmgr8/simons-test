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
    pairs = {}
    for x in numbers:
        if x in pairs:
            return x * pairs[x]
        pairs[2020 - x] = x


def three_numbers_to_2020(numbers: list[int]) -> int | None:
    """
    Get the product of three integers that adds to 2020

    :param numbers: list of integers
    :return: either an integer or None
    """
    n = len(numbers)
    triples = {}
    for i, x in enumerate(numbers):
        for j in range(i + 1, n):
            y = numbers[j]
            if y in triples:
                return y * triples[y][0] * triples[y][1]
            triples[2020 - x - y] = (x, y)



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
