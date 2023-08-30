# Imports
import argparse
import csv
from datetime import date
from tabulate import tabulate
from functions import new_id, give_bought_id, get_bought_id, add_sold_item, reset_date, check_if_sold

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    bought_csv_path = "data\\bought.csv"

    # Argparse Koekkoek's SuperPy
    parser = argparse.ArgumentParser(
        prog="Koekkoek's SuperPy",
        description="Welcome to your supermarket inventory software.",
        epilog="Questions? Feel free to ask: helpdesk@superpy.com",
    )

    # Create subparsers
    subparsers = parser.add_subparsers(dest="command")

    # Create buy parser
    buy_parser = subparsers.add_parser(
        "buy", help="Use buy to add products to your inventory."
    )

    buy_parser.add_argument("--product_name", type=str, help="Name of current product")
    buy_parser.add_argument("--product_price", type=float, help="Price of current product")
    buy_parser.add_argument("--expiration_date", type=str, help="Date of which current product expires")

    # Create reset date parser
    date_parser = subparsers.add_parser(
        "reset_date", help="Use to reset current date to today (%Y-%m-%d)"
    )

    # Create report parser
    report_parser = subparsers.add_parser(
        "report", help="Use 'report' to get a detailed report."
    )

    # Create report suberparser
    subparser_report = report_parser.add_subparsers(dest="get_report")

    # Create report inventory parser
    parser_report_inventory = subparser_report.add_parser("inventory", help="Get inventory report")
    parser_report_inventory.add_argument("--now", help="Get today's inventory report")
    parser_report_inventory.add_argument("--yesterday", help="Get yesterday's inventory report")

    # Create sell parser
    sell_parser = subparsers.add_parser(
        "sell", help="Use to sell a product."
    )
    sell_parser.add_argument("--product_name", type=str, help="Name of sold product")
    sell_parser.add_argument("--price", type=float, help="Price of sold product")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "reset_date":
        reset_date()

    elif args.command == "buy":
        # To do: checking if user gives 3 arguments?

        # Make a list of user input
        new_product = [
            new_id(),
            args.product_name,
            str(date.today()),
            args.product_price,
            args.expiration_date
        ]

        # Is it a valid list?
        if None in new_product:
            print("\nATTENTION: Invalid input.\n")
            print("Make sure you entered the following arguments: --product_name, --product_price, and --expiration_date.")
        else:
            # Open existing bought CSV file in append mode
            with open(bought_csv_path, mode='a') as file:
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

    elif args.command == "sell":
        # Make a list of sold product
        sold_product = [
            give_bought_id(),
            get_bought_id(args.product_name),
            str(date.today()),
            args.price
        ]
        # Is it a valid list?
        if None in sold_product:
            print("Make sure you entered the following arguments: --product_name and --price.")
        else:
            # Check if product is already sold
            not_yet_sold = check_if_sold(sold_product[1])
            if not_yet_sold:
                # Not yet sold? Then add list to sold.csv
                add_sold_item(sold_product)

    elif args.command == "report":
        if args.get_report == "inventory":
            # Make a report of current inventory.
            with open(bought_csv_path) as file:
                items = csv.reader(file)
                list_header = next(items)
                print(tabulate(items, headers=list_header, tablefmt="grid"))


if __name__ == "__main__":
    main()
