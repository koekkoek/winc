import main


def test_get_none():
    assert main.get_none() == None


def test_flatten_dict():
    test_list = main.flatten_dict({"a": 42, "b": 3.14})

    # Testen of het een lijst is
    assert isinstance(test_list, list)

    # Testen of het ook met 1 dict-element werkt
    assert main.flatten_dict({"modelnumber": 10}) == [10]

    # Testen of het met een lijst werkt
    assert test_list == [42, 3.14]

    # Testen of het met een list in een dict werkt
    assert main.flatten_dict({"a": [42, 350], "b": 3.14}) == [[42, 350], 3.14]

    # Testen of een dict in een dict werkt
    assert main.flatten_dict
    ({"a": {"inner_a": 42, "inner_b": 350}, "b": 3.14}) == [
        {"inner_a": 42, "inner_b": 350},
        3.14,
    ]
