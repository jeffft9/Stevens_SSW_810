import pytest

from UI import *


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
        "SHIFT", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)
