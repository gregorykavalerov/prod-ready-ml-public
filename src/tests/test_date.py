import pytest

from animal_shelter import data
from animal_shelter.data import convert_camel_case


def test_convert_camel_case():
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"


def test_for_exceptions():
    with pytest.raises(TypeError):
        convert_camel_case(1.0)
