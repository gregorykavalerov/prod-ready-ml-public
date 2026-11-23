import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


@pytest.fixture(scope="function")
def list_of_sex():
    return ["Spayed Female", "Neutered Male", "Intact Female"]


def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features._check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


def test_get_sex(list_of_sex):
    s = pd.Series(list_of_sex)
    result = features._get_sex(s)
    expected = pd.Series(["female", "male", "female"])
    assert_series_equal(result, expected)


def test_get_neutered(list_of_sex):
    s = pd.Series(list_of_sex)
    result = features._get_neutered(s)
    expected = pd.Series(["fixed", "fixed", "intact"])
    assert_series_equal(result, expected)


def test_get_hair_type():
    s = pd.Series(["Domestic Shorthair Mix", "Domestic Medium Hair Mix", "Beagle Mix"])
    result = features._get_hair_type(s)
    expected = pd.Series(["shorthair", "medium hair", "unknown"])
    assert_series_equal(result, expected)


def test_compute_days_upon_outcome():
    s = pd.Series(["6 months", "3 months"])
    result = features._compute_days_upon_outcome(s)
    print(result)
    expected = pd.Series([180.0, 90.0])
    assert_series_equal(result, expected)
