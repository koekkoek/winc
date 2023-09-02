# Imports
import argparse
import csv
from datetime import date
from tabulate import tabulate
from functions import (
    new_id,
    give_bought_id,
    get_bought_id,
    add_sold_item,
    reset_date,
    check_if_sold,
    count_by_product_name,
    advance_time,
    get_todays_inventory,
    get_yesterdays_inventory,
    get_revenue_report,
    get_profit_report,
    buy_product,
    sell_product,
    export_to_csv
)

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

    # Create parser for advancing time
    parser.add_argument(
        "--advance_time", type=int,
        help="Use to add days to advance current day")

    # Create buy parser
    buy_parser = subparsers.add_parser(
        "buy", help="Use buy to add products to your inventory."
    )

    buy_parser.add_argument(
        "--product_name", type=str,
        help="Name of current product")
    buy_parser.add_argument(
        "--product_price", type=float,
        help="Price of current product")
    buy_parser.add_argument(
        "--expiration_date", type=str,
        help="Date of which current product expires")

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

    # Create sell parser
    sell_parser = subparsers.add_parser(
        "sell", help="Use to sell a product."
    )
    sell_parser.add_argument(
        "--product_name", type=str, help="Name of sold product")
    sell_parser.add_argument(
        "--price", type=float, help="Price of sold product")

    # Create report inventory parser
    parser_report_inventory = subparser_report.add_parser(
        "inventory", help="Get inventory report")
    parser_report_inventory.add_argument(
        "--now", action="store_true",
        help="Get today's inventory report")
    parser_report_inventory.add_argument(
        "--yesterday", action="store_true",
        help="Get yesterday's inventory report")
    parser_report_inventory.add_argument(
        "--by_type", action="store_true",
        help="Current items in bought.csv file, ordered by product name")
    parser_report_inventory.add_argument(
        "--export", action="store_true",
        help="Use to export data in CSV file"
    )

    # Create revenue parser
    revenue_report_parser = subparser_report.add_parser(
        "revenue", help="Use to get revenue")
    revenue_report_parser.add_argument(
        "--today", action="store_true",
        help="Get today's revenue report")
    revenue_report_parser.add_argument(
        "--yesterday", action="store_true",
        help="Get yesterday's revenue report")
    revenue_report_parser.add_argument(
        "--date", help="Get revenue report of specific date"
    )

    # Create profit parser
    profit_report_parser = subparser_report.add_parser(
        "profit", help="Use to get profit"
    )
    profit_report_parser.add_argument(
        "--today", action="store_true",
        help="Get today's profit report")
    profit_report_parser.add_argument(
        "--yesterday", action="store_true",
        help="Get yesterday's profit report")
    profit_report_parser.add_argument(
        "--date", help="Get profit report of specific date"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.advance_time:
        advance_time(args.advance_time)

    elif args.command == "reset_date":
        reset_date()

    elif args.command == "buy":
        buy_product(args.product_name, args.product_price,
                    args.expiration_date)

    elif args.command == "sell":
        sell_product(args.product_name, args.price)

    elif args.get_report == "inventory":
        if args.export:
            list = {"now": args.now, "yesterday": args.yesterday}
            for key, value in list.items():
                if value == True:
                    category = key
            export_to_csv(category)
        # Make report for how many of each type of product
        # the supermarket currently holds
        elif args.by_type is True:
            count_by_product_name()
        # Make a report of current inventory
        elif args.now:
            get_todays_inventory()
        # Make a report of yesterday's inventory
        elif args.yesterday:
            get_yesterdays_inventory()
        # Print a list of all items in inventory
        else:
            with open(bought_csv_path) as file:
                items = csv.reader(file)
                list_header = next(items)
                print(tabulate(items, headers=list_header, tablefmt="grid"))

    elif args.get_report == "revenue":
        # Get today's revenue report
        if args.today:
            revenue = get_revenue_report("today")
            if revenue == 0:
                print("We haven't sold anything yet today.")
            elif revenue > 0:
                print(f"Today's revenue so far: {revenue}")
        # Get yesterday's revenue report
        elif args.yesterday:
            revenue = get_revenue_report("yesterday")
            if revenue == 0:
                print("We haven't sold anything yesterday.")
            elif revenue > 0:
                print(f"Yesterday's revenue: {revenue}")
        # Get revenue report of specific date
        elif args.date:
            revenue = get_revenue_report(args.date)
            if revenue == 0:
                print(f"Revenue on {args.date}: € 0,-")
            elif revenue > 0:
                print(f"Revenue on {args.date}: {revenue}")
        # No arguments? Show some help
        else:
            revenue_report_parser.print_help()

    elif args.get_report == "profit":
        # Get today's profit report
        if args.today:
            profit = get_profit_report("today")
            if profit == 0:
                print("No profit today...")
            elif profit > 0:
                print(f"Today's profit: {round(profit, 2)}")
        # Get yesterday's profit report
        elif args.yesterday:
            profit = get_profit_report("yesterday")
            if profit == 0:
                print("No profit yesterday...")
            elif profit > 0:
                print(f"Yesterday's profit: {round(profit, 2)}")
        # Get profit report of specific date
        elif args.date:
            profit = get_profit_report(args.date)
            if profit == "False":
                print(profit_report_parser.print_help())
            elif profit == 0:
                print(f"No profit on {args.date}...")
            elif profit > 0:
                print(f"Profit on {args.date}: {round(profit, 2)}")
        # No arguments? Show some help
        else:
            profit_report_parser.print_help()


if __name__ == "__main__":
    main()
