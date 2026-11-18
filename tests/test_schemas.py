from app.schemas.url import UrlCreate
import pytest
from pydantic import ValidationError

def test_too_short_alias_is_rejected():
    with pytest.raises(ValidationError):
        UrlCreate(target_url="https://example.com", alias="a")



def test_alias_with_symbol_is_rejected():
    with pytest.raises(ValidationError):
        UrlCreate(target_url = "https://example.com", alias= "a%%")



def test_alias_with_underscore_is_rejected():
    with pytest.raises(ValidationError):
        UrlCreate(target_url="https://example.com", alias="a_b_c")


def test_reserved_alias_is_rejected():
    with pytest.raises(ValidationError):
        UrlCreate(target_url = "https://example.com", alias = "health")


def test_valid_alias_is_accepted():
        result = UrlCreate(target_url = "https://example.com", alias = "promo")
        assert result.alias == "promo"