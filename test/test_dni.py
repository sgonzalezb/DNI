from src.dni import *

def test_number_length():
    assert False == Dni('555555555').validate_dni()
    assert False == Dni('56423323324332').validate_dni()
    assert False == Dni('47273175').validate_dni()

def test_validate_letter():
    assert "J" == Dni(43460514).get_letter()
    assert "N" == Dni(43460513).get_letter()
    assert "W" == Dni(43066766).get_letter()

def test_validate_dni():
    assert "43460514J" == Dni("43460514").get_dni()
    assert "43460513N" == Dni("43460513").get_dni()
    assert "43066766W" == Dni("43066766W").get_dni()

