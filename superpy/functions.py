def give_bought_id():
    """Check last ID number in bought.csv file. Add 1 and return next new ID
    """
    with open("data\\bought.csv") as csv_file:
        last_line = csv_file.readlines()[-1]

        try:
            last_line_number = int(last_line[0])
            return last_line_number + 1
        except Exception:
            return 1

        # Pay Attention: should I always return 1? Can cause problems
        # Should I fist check if first line exist? If not: make it?


def latest_product_id():
    """Function to read latest product id"""
    with open("data\\id.txt") as file:
        id = file.read()
        if id == "":
            id = 0
        print(f"Current id: {id}")
        return id


def new_id():
    """Function to create new product id"""
    with open("data\\id.txt", "r+") as file:
        # Get last used product ID
        current_id = file.read()
        # If there isn't a product ID, make it 0
        if current_id == "":
            current_id = 0
        # Add 1 to the current ID
        new_id = int(current_id) + 1
        # Rewind
        file.seek(0)
        file.write(str(new_id))


if __name__ == "__main__":
    # print(give_bought_id())
    print(latest_product_id())
    # new_id()
