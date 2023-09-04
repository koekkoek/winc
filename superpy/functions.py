import csv
import time
import json
from rich.progress import Progress
from rich import print as rprint
from re import search as rsearch
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
            msg = "\n:warning:  [bold red]ATTENTION:[/bold red] "
            msg += f"There is no {product_name}\n"
            rprint(msg)
            return None
        # One item in list? Return ID
        elif len(found) == 1:
            return found[0]
        # Multiple items in list? Return all
        else:
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


def buy_product(product_name, product_price, expiration_date):
    """Use to buy a product and add it to bought.csv"""
    # Make a list of user input
    new_product = [
        new_id(),
        product_name,
        str(date.today()),
        product_price,
        expiration_date
        ]
    # Is it a valid list?
    if None in new_product:
        print("\nATTENTION: Invalid input.\n")
        print("Make sure you entered the following arguments:")
        print("\t--product_name, --product_price, and --expiration_date.\n")
    else:
        # Open existing bought CSV file in append mode
        with open(bought_path, mode='a') as file:
            # Pass this file object to csv.writer()
            # and get a writer object
            add_product = csv.writer(file, delimiter=',', lineterminator='\n')
            # Pass the list as an argument into
            # the writerow()
            add_product.writerow(new_product)
            # Message when succesfull
            print("\n=====================================")
            print("Added the following list of items:\n")
            n = 0
            for item in ["ID", "name", "date", "price", "expiration date"]:
                print(f"Product {item}: {new_product[n]}")
                n += 1
            print("=====================================\n")


def sell_product(product_name, product_price):
    """Use to sell a product and add item to sold.csv list"""
    # Make a list of sold product
    sold_product = [
        give_bought_id(),
        get_bought_id(product_name),
        str(date.today()),
        product_price
    ]
    # Is it a valid list?
    if None in sold_product:
        print("Make sure you entered the following arguments:")
        print("\t--product_name and --price.\n")
    else:
        # Check if product is already sold
        not_yet_sold = check_if_sold(sold_product[1])
        if not_yet_sold:
            # Not yet sold? Then add list to sold.csv
            add_sold_item(sold_product)


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
    return product_per_type


def get_todays_inventory():
    """Get today's inventory and show to user"""
    inventory = []
    date = date_to_datetime(get_current_date())
    with open(bought_path) as file:
        items = csv.DictReader(file)
        for item in items:
            item_buy_date = datetime.strptime(
                item['buy_date'], '%Y-%m-%d').date()
            item_expiration_date = datetime.strptime(
                item['expiration_date'], '%Y-%m-%d').date()
            # Get items in bought.csv who aren't expired
            # And check if item isn't in sold.csv list
            if date > item_buy_date and (
                item_expiration_date > date) and (
                    check_if_sold(item['id'])):
                inventory.append(item)
    return inventory


def get_yesterdays_inventory():
    """Get yesterday's inventory and show to user"""
    inventory = []
    date = date_to_datetime(get_current_date()) - timedelta(days=1)
    with open(bought_path) as file:
        items = csv.DictReader(file)
        for item in items:
            item_buy_date = datetime.strptime(
                item['buy_date'], '%Y-%m-%d').date()
            item_expiration_date = datetime.strptime(
                item['expiration_date'], '%Y-%m-%d').date()
            # Get items in bought.csv who aren't expired
            # And check if item isn't in sold.csv list
            if date > item_buy_date and (
                item_expiration_date > date) and (
                    check_if_sold(item['id'])):
                inventory.append(item)
    return inventory


def make_table(inventory):
    """Show inventory in beautiful table"""
    if inventory:
        print(tabulate(inventory, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No inventory.")


def get_expired_products():
    """Get expired products which aren't sold"""
    current_date = date_to_datetime(get_current_date())
    expired_products = []
    with open(bought_path) as bought_file:
        # Get list of bought products
        bought_items = csv.DictReader(bought_file)
        for item in bought_items:
            # Check if an item is expired.
            # If so: is it sold?
            # Expired and not sold? Append to expired_products list
            item_expiration = date_to_datetime(item['expiration_date'])
            if current_date > item_expiration and check_if_sold(item['id']):
                expired_products.append(item)
    return expired_products


def get_revenue_report(when):
    """Get reveneu report of today, yesterday or specific date"""
    total_revenue = 0
    if when == "today":
        date = get_current_date()
    elif when == "yesterday":
        date = date_to_datetime(get_current_date())
        date = date - timedelta(days=1)
    else:
        date = datetime.strptime(when, '%Y-%m-%d').date()
    # Open sold file
    with open(sell_path) as sell_file:
        sold_items = csv.DictReader(sell_file)
        # Iterate over sold items
        for item in sold_items:
            # Check is sold date is the same as today
            if item['sell_date'] == str(date):
                total_revenue += float(item['sell_price'])
    return total_revenue


def get_profit_report(when):
    """Get profit report of today, yesterday or specific date"""
    total_revenue = 0
    total_buy_price = 0
    bought_check = []
    if when == "today":
        date = get_current_date()
    elif when == "yesterday":
        date = date_to_datetime(get_current_date())
        date = date - timedelta(days=1)
    else:
        try:
            date = datetime.strptime(when, '%Y-%m-%d').date()
        except ValueError:
            return 'False'
            date = date_to_datetime("2000-01-01")
    # Open sold file
    with open(sell_path) as sell_file:
        sold_items = csv.DictReader(sell_file)
        # Iterate over sold items
        for item in sold_items:
            # Check is sold date is the same as today
            if item['sell_date'] == str(date):
                total_revenue += float(item['sell_price'])
                bought_check.append(item['bought_id'])
    # Open bought file and count buy prices
    with open(bought_path) as bought_file:
        bought_items = csv.DictReader(bought_file)
        # Iterate over bought items
        for item in bought_items:
            # Check: is id in bought_check list?
            if item['id'] in bought_check:
                # Add price to total_buy_price
                total_buy_price += float(item['buy_price'])
    # Calculate profit price (revenue - buy_price)
    profit = total_revenue - total_buy_price
    return profit


def reset_date(new_date):
    """Function to reset current_day.txt to new date"""
    with open(date_path, mode="w") as file:
        file.write(new_date)
        rprint(f"Current date succesfully updated: {new_date}")
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
        date_datetime = date_to_datetime(current_date)
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
    dateformat = datetime.strptime(date, '%Y-%m-%d').date()
    return dateformat


def export_to_csv(category):
    """Export inventory report data to CSV file"""
    date_id = datetime.today().date()
    file_name = f"exports\\csv_report_{date_id}.csv"
    if category == "now":
        data = get_todays_inventory()
    elif category == "yesterday":
        data = get_yesterdays_inventory()
    field_names = ['id', 'product_name', 'buy_price',
                   'buy_date', 'expiration_date']
    with open(file_name, mode="w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    with Progress() as progress:
        task1 = progress.add_task("[green]Exporting...", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.9)
            time.sleep(0.02)
    msg = "[green]Finished![/green] Data exported to "
    msg += f"[u purple]{file_name}[/u purple]"
    rprint(msg)


def export_to_json(category):
    """Export inventory report data to json file"""
    date_id = datetime.today().date()
    file_name = f"exports\\json_report_{date_id}.json"
    if category == "now":
        data = get_todays_inventory()
        # data_json = json.dumps(data, indent=4)
    elif category == "yesterday":
        data = get_yesterdays_inventory()
        # data_json = json.dumps(data, indent=4)
    with open(file_name, mode="w", newline='') as json_file:
        json.dump(data, json_file, indent=4)
    with Progress() as progress:
        task1 = progress.add_task("[green]Exporting...", total=100)
        while not progress.finished:
            progress.update(task1, advance=0.9)
            time.sleep(0.02)
    msg = "[green]Finished![/green] JSON data exported to "
    msg += f"[u purple]{file_name}[/u purple]"
    rprint(msg)


def it_is_a_valid_input(category, input):
    """Function to check if users input contains valid data."""
    # Define Regular Expressions
    valid_date_data = "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    valid_text = "^[a-zA-Z0-9_]+$"
    # Check users input for valid date
    if category == "date":
        return rsearch(valid_date_data, input)
    if category == "product_name":
        return rsearch(valid_text, input)


def import_new_data():
    """Function to import standard data to try superpy as a demo"""
    # Get bought data in JSON format
    with open("import\\json_bought.json") as json_file:
        json_data = json.load(json_file)
    # Add JSON data to CSV bought file
    with open(bought_path, mode="w", newline="") as bought_file:
        csv_writer = csv.writer(bought_file)
        # Count var for writing headers to CSV file
        count = 0
        for row in json_data:
            if count == 0:
                header = row.keys()
                csv_writer.writerow(header)
                count += 1
            # Writing JSON data to CSV file
            csv_writer.writerow(row.values())
    # Get sold data in JSON format
    with open("import\\json_sold.json") as json_file:
        json_data = json.load(json_file)
    # Add JSON data to CSV data file
    with open(sell_path, mode="w", newline="") as sold_file:
        csv_writer = csv.writer(sold_file)
        # Count var for writing headers to CSV file
        count = 0
        for row in json_data:
            if count == 0:
                header = row.keys()
                csv_writer.writerow(header)
                count += 1
            # Writing JSON data to CSV file
            csv_writer.writerow(row.values())
    # Set date
    with open("import\\standard_day.txt") as day_file:
        day_data = day_file.read()
        if day_data == "":
            day_data = "2023-09-07"
    with open("data\\current_day.txt", mode="w") as current_day:
        current_day.write(day_data)
    # Set id
    with open("import\\standard_id.txt") as id_file:
        id_data = id_file.read()
        if id_data == "":
            id_data = "30"
    with open("data\\id.txt", mode="w") as current_id:
        current_id.write(id_data)
    # Print succes message
    rprint("[green]Succesfully[/green] imported all data to csv file.")


if __name__ == "__main__":
    # print(give_bought_id())
    # print(latest_product_id())
    # new_id()
    # print(get_bought_id("tomato"))
    # reset_date()
    # print(check_if_sold('27'))
    # count_by_product_name()
    # print(advance_time(2))
    # get_todays_inventory()
    # print(get_current_date())
    # print(date_to_datetime("2022-01-02"))
    # get_revenue_report("2023-10-01")
    # print(get_profit_report("2023-08-30"))
    # print(get_profit_report("today"))
    # export_to_csv("now")
    # get_bought_id('bananaaaa')
    make_table(get_expired_products())
