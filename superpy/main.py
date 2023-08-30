# Imports
import argparse
import csv
from datetime import date
from functions import give_bought_id

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
    buy_parser.add_argument("--product_expiration_date", type=str, help="Date of which currenr product expires")

    # Parse arguments

    args = parser.parse_args()

    if args.command == "buy":
        # To do: checking if user gives 3 arguments?

        # Make a list of user input
        new_product = [
            give_bought_id(),
            args.product_name,
            str(date.today()),
            args.product_price,
            args.product_expiration_date
        ]

        # Is it a valid list?
        if None in new_product:
            raise TypeError("Invalid input")
        else:
            # Open existing bought CSV file in append mode
            with open(bought_csv_path, mode='a') as file:
                # Pass this file object to csv.writer()
                # and get a writer object
                add_product = csv.writer(file, delimiter=',', lineterminator='\n')

                # Pass the list as an argument into
                # the writerow()
                add_product.writerow(new_product)

                # Close the file object
                file.close()


if __name__ == "__main__":
    main()
