import sys
from typing import NamedTuple
from contextlib import suppress

import pytest


class StringData(NamedTuple):
    start: int
    end: int
    char: str
    string: str


def load_input(fname: str) -> list[StringData]:
    """
    Load input data from the given file

    :param fname: input file name
    :return: list of StringData
    """
    data = []
    with open(fname) as fhandle:
        for line in fhandle:
            chunks = line.split()
            start, end = [int(x) for x in chunks[0].split('-')]
            char = chunks[1][0]
            string = chunks[2]
            data.append(StringData(start, end, char, string))
    return data


def valid_strings_by_occurance(data: list[StringData]) -> int:
    """
    Get number of strings that has valid number of given character occurances

    :param numbers: list of StringData
    :return: the number of valid strings
    """
    n_valid = 0
    for row in data:
        count = 0
        for c in row.string:
            count += int(c == row.char)
        if row.start <= count <= row.end:
            n_valid += 1

    return n_valid


def valid_strings_by_position(data: list[StringData]) -> int:
    """
    Get number of strings that has valid position of given character in them

    :param numbers: list of StringData
    :return: the number of valid strings
    """
    n_valid = 0
    for row in data:
        with suppress(IndexError):
            if row.string[row.start] == row.char:
                n_valid += 1
                continue

        with suppress(IndexError):
            if row.string[row.end] == row.char:
                n_valid += 1

    return n_valid



def main(input_file='input/input2.txt'):
    data = load_input(input_file)
    print(valid_strings_by_occurance(data))
    print(valid_strings_by_position(data))


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])


@pytest.fixture
def input_data():
    return [
        StringData(1, 3, 'a', 'abcde'),
        StringData(1, 3, 'b', 'cdefg'),
        StringData(2, 9, 'c', 'ccccccccc'),
    ]


def test_valid_strings_by_occurance(input_data):
    assert valid_strings_by_occurance(input_data) == 2


def test_valid_strings_by_position(input_data):
    assert valid_strings_by_position(input_data) == 1
