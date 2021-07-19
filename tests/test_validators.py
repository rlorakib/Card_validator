from card_validator.validator import get_issuer
import pytest

def test_get_issuer_visa():
    assert get_issuer("4125 6524 6842 1024") =="Visa"

def test_get_issuer_mastercard():
    assert get_issuer("5120 5792 2354 9832") =="MasterCard"
    with pytest.raises(ValueError):
      get_issuer("5620 5792 2354 9832")

def test_get_issuer_american_express():
    assert get_issuer("3710 2049 6587 201") =="American Express"
    with pytest.raises(ValueError):
      get_issuer("3210 2049 6587 201")

def test_length():
    with pytest.raises(ValueError):
      get_issuer("4110 2541 3978 3895 4")
    with pytest.raises(ValueError):
      get_issuer("5610 2541 3978 3895 1")
    with pytest.raises(ValueError):
      get_issuer("3710 2049 6587 2012")

    with pytest.raises(ValueError):
      get_issuer("4110 2541 3978 389")
    with pytest.raises(ValueError):
      get_issuer("5610 2541 3978 389")
    with pytest.raises(ValueError):
      get_issuer("3710 2541 3978 38")
