def get_none():
    return None


def flatten_dict(items_dict):
    new_list = []

    # Iteraten door meegegeven dict
    for k, v in items_dict.items():
        # Checken of item een dict is
        if isinstance(items_dict[k], dict):
            # Recursion uitvoeren op gevonden dict
            new_list += flatten_dict(items_dict[k])
        # Item is geen dict, dus toevoegen aan de lijst
        else:
            new_list.append(v)
    return new_list


if __name__ == "__main__":
    print(flatten_dict({"a": {"inner_a": 42, "inner_b": 350}, "b": 3.14}))
    print(flatten_dict({"a": 42, "b": 3.14}))
