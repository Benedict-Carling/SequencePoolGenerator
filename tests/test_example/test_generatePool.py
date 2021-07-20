"""Tests for hello function."""
import pytest

from sequencegenerator.generatePool import generatePool


def test_generatePool():
    """Example test with parametrization."""
    my_pool = generatePool(input_sequence='ACACAGTCATCGATCGXXXXXACAGCCXXXXXXGAC',initial_temperature=8, iteration_length=1000, Tm_flexibility=5, GC_flexibility=5, poolLength=3)
    assert len(my_pool) == 3
