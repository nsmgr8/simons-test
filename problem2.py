import sys
from typing import Callable, NamedTuple
from contextlib import suppress

import pytest


class StringData(NamedTuple):
    start: int
    end: int
    char: str
    string: str

    @staticmethod
    def from_string(input_string: str) -> 'StringData':
        """
        Factory to create a StringData instance from a formatted string

        :param input_string: formatted string, e.g., '1-3 a: abcde'
        :return: StringData instance created from the input_string
        """
        chunks = input_string.split()
        start, end = [int(x) for x in chunks[0].split('-')]
        char = chunks[1][0]
        string = chunks[2]
        return StringData(start, end, char, string)

    def validate(self, strategy: Callable[['StringData'], bool]) -> bool:
        return strategy(self)


def valid_by_occurance(data: StringData) -> bool:
    """
    :return: True if the string is valid by the number of occurances
        condition, False otherwise
    """
    count = sum(int(c == data.char) for c in data.string)
    return data.start <= count <= data.end


def valid_by_position(data: StringData) -> bool:
    """
    :return: True if the string is valid by position of the character in
        the string, False otherwise
    """
    n_found = 0
    with suppress(IndexError):
        n_found += int(data.string[data.start - 1] == data.char)
    with suppress(IndexError):
        n_found += int(data.string[data.end - 1] == data.char)
    return n_found == 1


def load_input(fname: str) -> list[StringData]:
    """
    Load input data from the given file

    :param fname: input file name
    :return: list of StringData
    """
    data = []
    with open(fname) as fhandle:
        data = [StringData.from_string(line) for line in fhandle]
    return data


def valid_strings_by_occurance(data: list[StringData]) -> int:
    """
    Get number of strings that has valid number of given character occurances

    :param numbers: list of StringData
    :return: the number of valid strings
    """
    return sum(int(x.validate(valid_by_occurance)) for x in data)


def valid_strings_by_position(data: list[StringData]) -> int:
    """
    Get number of strings that has valid position of given character in them

    :param numbers: list of StringData
    :return: the number of valid strings
    """
    return sum(int(x.validate(valid_by_position)) for x in data)



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


def test_factory_from_string():
    data = StringData.from_string('1-3 a: aba')
    assert data.start == 1
    assert data.end == 3
    assert data.char == 'a'
    assert data.string == 'aba'


def test_valid_occurances():
    assert StringData(1, 3, 'a', 'abcde').validate(valid_by_occurance)
    assert not StringData(1, 3, 'b', 'cdefg').validate(valid_by_occurance)


def test_valid_positions():
    assert StringData(1, 3, 'a', 'abcde').validate(valid_by_position)
    assert not StringData(1, 3, 'b', 'cdefg').validate(valid_by_position)
    assert not StringData(2, 9, 'c', 'ccccccccc').validate(valid_by_position)
