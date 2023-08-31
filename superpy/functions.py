import csv
from datetime import date, datetime, timedelta
from tabulate import tabulate

bought_path = "data\\bought.csv"
sell_path = "data\\sold.csv"
date_path = "data\\current_day.txt"


def give_bought_id():
    """Check last ID number in bought.csv file. Add 1 and return next new ID
    """
    with open(sell_path) as csv_file:
        dict_items = csv.DictReader(csv_file)
        last_item_list = list(dict_items)
        last_item = int(last_item_list[-1]['id'])
        if last_item >= 0:
            return last_item + 1
        else:
            return 1
        # Pay Attention: should I always return 1? Can it cause problems?
        # Should I fist check if first line exist? If not: make it?


def get_bought_id(product_name):
    """Function to get the Product ID of a sold product"""
    # What if there are multiple products with the same name?
    with open(bought_path) as csv_file:
        items = csv.reader(csv_file)
        found = []
        # Search for product name. Found? Add ID to 'found' list
        for item in items:
            if item[1] == product_name:
                found.append(item[0])
        # No items in list? Return None
        if len(found) == 0:
            print(f'\nATTENTION: There is no {product_name}\n')
            return None
        # One item in list? Return ID
        elif len(found) == 1:
            return found[0]
        # Multiple items in list? Return all
        else:
            # To do: what to do with multiple products? Return all?
            return found[0]


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
        return new_id


def add_sold_item(sold_product):
    """Function to sell a product and append it in sold.csv file"""
    with open(sell_path, mode="a") as file:
        # Pass file object to csv.writer
        add_sold_product = csv.writer(file, delimiter=',', lineterminator='\n')

        # Pass the list to file
        add_sold_product.writerow(sold_product)

        # Message when succesfull
        print("\n=====================================")
        print("Product sold:\n")
        n = 0
        for item in ["ID", "Bought_id", "selldate", "sell price"]:
            print(f"Product {item}: {sold_product[n]}")
            n += 1
        print("=====================================\n")


def check_if_sold(product_sold_id):
    """Check if sold ID already is in sold.csv? If so, then the product
    is already sold."""
    with open(sell_path) as file:
        rows = csv.DictReader(file)
        # By default: product isn't sold already. So 'not_yet_sold' is True.
        not_yet_sold = True
        for row in rows:
            # Checking for product_sold_id in sold.csv list.
            if row['bought_id'] == product_sold_id:
                # If it is in the list. Then switch 'not_yet_sold' to False.
                not_yet_sold = False
                # print("\nATTENTION: Product already on sold list.\n") # TO DO: melding elders toevoegen.
                break
        return not_yet_sold


def count_by_product_name():
    """Function to count quantity by product name"""
    with open(bought_path) as file:
        # Make a list and dict
        product_type = []
        product_per_type = {}
        products = csv.reader(file)
        # Iterate over products and append them in list
        for product in products:
            product_type.append(product[1])
        # Iterate over list and add them in dict
        for item in product_type[1:]:
            if item not in product_per_type:
                product_per_type[item] = 1
            elif item in product_per_type:
                product_per_type[item] = product_per_type[item]+1
        # Print results
        print("============================")
        print("Current quantity per product:\n")
        for k, v in product_per_type.items():
            print(f"{k}: {v}")
        print("\n============================")


def get_todays_inventory():
    """Get today's inventory and show to user"""
    inventory = []
    date = date_to_datetime(get_current_date())
    with open(bought_path) as file:
        items = csv.DictReader(file)
        for item in items:
            item_date = datetime.strptime(item['expiration_date'], '%Y-%m-%d').date()
            # Get items in bought.csv who aren't expired
            # And check if item isn't in sold.csv list
            if item_date > date and check_if_sold(item['id']):
                inventory.append(item)
    print(tabulate(inventory, headers="keys", tablefmt="grid"))


def reset_date():
    """Function to reset date to current date"""
    with open(date_path, mode="w") as file:
        new_date = date.today().strftime('%Y-%m-%d')
        file.write(new_date)
        print(f"Current date succesfully updated: {new_date}")
        return new_date


def advance_time(number_of_days: int):
    """Function to advance days with users input"""
    if number_of_days <= 0:
        print("Please use a positive number.")
        return False
    with open(date_path, mode="r+") as file:
        # Get current date
        current_date = file.read()
        # Get current date in datetime format
        date_datetime = datetime.strptime(current_date, '%Y-%m-%d').date()
        # Add days
        new_date = date_datetime + timedelta(days=number_of_days)
        # Change datetime format back to string
        new_date = new_date.strftime('%Y-%m-%d')
        # Write new date in file
        file.seek(0)
        file.write(new_date)
        # Return message
        msg = f"Numbers of days added: {number_of_days}.\n"
        msg += f"New current date: {new_date}"
        return msg


def get_current_date():
    """Open current_day.txt and return date"""
    with open(date_path) as file:
        date = file.read()
        return date


def date_to_datetime(date):
    """Formate date text to datetime object"""
    # TO DO: Check users input / try?
    dateformat = datetime.strptime(date, '%Y-%m-%d').date()
    return dateformat


if __name__ == "__main__":
    # print(give_bought_id())
    # print(latest_product_id())
    # new_id()
    # print(get_bought_id("tomato"))
    # reset_date()
    # print(check_if_sold('27'))
    # count_by_product_name()
    # print(advance_time(2))
    get_todays_inventory()
    # print(get_current_date())
    #print(date_to_datetime("2022-01-02"))
