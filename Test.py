import pytest

from UI import *
from Dictionary import *


def test_both_empty():
    result = checkInput("sonar")
    assert(result == True)


def test_upper():
    result = checkInput("SONAR")
    assert(result == True)


def test_empty():
    result = checkInput("")
    assert(result == False)


def test_num():
    result = checkInput("12345")
    assert(result == False)


def test_word_used_one():
    result = checkWordUsed(
        "sonar".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_two():
    result = checkWordUsed(
        "SONAR".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_three():
    result = checkWordUsed(
        "SHIFT", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)


def test_word_used_four():
    result = checkWordUsed(
        "", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)


def test_word_length_one():
    result = checkWordLength(
        "     ")
    assert(result == False)


def test_word_length_two():
    result = checkWordLength(
        "")
    assert(result == False)


def test_word_length_three():
    result = checkWordLength(
        "SONAR")
    assert(result == True)


def test_word_length_three():
    result = checkWordLength(
        "SON")
    assert(result == False)


def test_word_length_three():
    result = checkWordLength(
        "SONARSONARSONAR")
    assert(result == False)


def test_dict_word_length():
    todays_word, word_list = getRandomWord()
    assert(len(todays_word) == 5)


def test_word_in_dict():
    todays_word, word_list = getRandomWord()
    assert(todays_word in word_list)
