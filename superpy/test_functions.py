from functions import give_bought_id, get_bought_id, latest_product_id, new_id, reset_date
from datetime import date


def test_give_bought_id():
    assert type(give_bought_id()) == int
    assert give_bought_id() >= 0


def test_get_bought_id():
    assert get_bought_id("tomatoooooo") == None
    assert get_bought_id("tomato") == '24'  # Change when edited
    assert get_bought_id("banana") == '27'  # Change when edited


def test_latest_product_id():
    assert type(int(latest_product_id())) == int
    assert int(latest_product_id()) >= 0


def test_new_id():
    assert type(int(new_id())) == int
    assert new_id() >= 0

def test_reset_date():
    assert reset_date() == str(date.today())
