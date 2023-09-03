# Imports
import argparse
import csv
from re import search as rsearch
from rich import print as rprint
from functions import (
    reset_date,
    count_by_product_name,
    advance_time,
    get_todays_inventory,
    get_yesterdays_inventory,
    get_revenue_report,
    get_profit_report,
    buy_product,
    sell_product,
    export_to_csv,
    get_expired_products,
    make_table
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

    # Create subparser
    subparser = parser.add_subparsers(
        dest="command",
        title="subcommands",
        description="Subcommands",
        help="Additional help")

    # Create parser for advancing time
    time_parser = subparser.add_parser(
        "advance_time",
        help="Use to add days to advance current day")
    time_parser.add_argument(
        "days",
        help="Add number of days to advance and set as new today"
    )

    # Create reset date parser
    date_parser = subparser.add_parser(
        "set_date",
        help="Use to set new date"
    )
    date_parser.add_argument(
        "date",
        type=str,
        help="Use YYYY-MM-DD for new date"
    )

    # Create buy parser
    buy_parser = subparser.add_parser(
        "buy",
        help="Buy product and add it to your inventory."
    )
    buy_parser.add_argument(
        "--product_name",
        type=str,
        required=True,
        help="Name of new product")
    buy_parser.add_argument(
        "--product_price",
        type=float,
        required=True,
        help="Price of new product")
    buy_parser.add_argument(
        "--expiration_date",
        type=str,
        required=True,
        help="Date on which new product expires")

    # Create sell parser
    sell_parser = subparser.add_parser(
        "sell",
        help="Use to sell a product."
    )
    sell_parser.add_argument(
        "--product_name",
        required=True,
        type=str,
        help="Name of sold product")
    sell_parser.add_argument(
        "--price",
        required=True,
        type=float,
        help="Price of sold product")

    # Create report parser
    report_parser = subparser.add_parser(
        "report",
        help="Use 'report' to get a detailed report."
    )

    # Create report suberparser
    subparser_report = report_parser.add_subparsers(
        dest="report_type",
        help="Report types")

    # Create report inventory parser
    parser_report_inventory = subparser_report.add_parser(
        "inventory",
        help="Get inventory report")
    parser_report_inventory.add_argument(
        "--now",
        action="store_true",
        help="Get today's inventory report")
    parser_report_inventory.add_argument(
        "--yesterday",
        action="store_true",
        help="Get yesterday's inventory report")
    parser_report_inventory.add_argument(
        "--by_type",
        action="store_true",
        help="Current items in bought.csv file, ordered by product name")
    parser_report_inventory.add_argument(
        "--expired",
        action="store_true",
        help="Get list of expired products.")
    parser_report_inventory.add_argument(
        "--export",
        action="store_true",
        help="Use to export data in CSV file"
    )

    # Create revenue parser
    revenue_report_parser = subparser_report.add_parser(
        "revenue",
        help="Use to get revenue report")
    revenue_report_parser.add_argument(
        "--today",
        action="store_true",
        help="Get today's revenue report")
    revenue_report_parser.add_argument(
        "--yesterday",
        action="store_true",
        help="Get yesterday's revenue report")
    revenue_report_parser.add_argument(
        "--date",
        help="Get revenue report of specific date"
    )

    # Create profit parser
    profit_report_parser = subparser_report.add_parser(
        "profit",
        help="Use to get profit"
    )
    profit_report_parser.add_argument(
        "--today",
        action="store_true",
        help="Get today's profit report")
    profit_report_parser.add_argument(
        "--yesterday",
        action="store_true",
        help="Get yesterday's profit report")
    profit_report_parser.add_argument(
        "--date",
        help="Get profit report of specific date"
    )

    # Parse arguments
    args = parser.parse_args()

    if args.command == "set_date":
        valid_date = rsearch("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", args.date)
        if valid_date:
            reset_date(args.date)
        else:
            msg = f"[bold red]'{args.date}'[/bold red] is an invalid input. "
            msg += "Use this format: [green]YYYY-MM-DD[/green]"
            rprint(msg)

    elif args.command == "advance_time":
        advance_time(args.advance_time)

    elif args.command == "buy":
        buy_product(args.product_name, args.product_price,
                    args.expiration_date)

    elif args.command == "sell":
        sell_product(args.product_name, args.price)

    elif args.command == "report":
        if args.report_type == "inventory":
            if args.export:
                category = False
                list = {"now": args.now, "yesterday": args.yesterday}
                for key, value in list.items():
                    if value:
                        category = key
                if category:
                    export_to_csv(category)
            # Make report for how many of each type of product
            # the supermarket currently holds
            elif args.by_type is True:
                count_by_product_name()
            # Make a report of current inventory
            elif args.now:
                make_table(get_todays_inventory())
            # Make a report of yesterday's inventory
            elif args.yesterday:
                make_table(get_yesterdays_inventory())
            elif args.expired:
                print("\nThe following items are expired and not sold:\n")
                make_table(get_expired_products())
            # Print a list of all items in inventory
            else:
                with open(bought_csv_path) as file:
                    items = csv.DictReader(file)
                    make_table(items)

        elif args.report_type == "revenue":
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

        elif args.report_type == "profit":
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
                revenue_report_parser.print_help()
    # No arguments? Show some help
    else:
        profit_report_parser.print_help()


if __name__ == "__main__":
    main()
