from functions import give_bought_id


def test_give_bought_id():
    assert type(give_bought_id()) == int
