# SuperPy
SuperPy is a command-line based inventory management tool designed to keep track of supermarket products. It provides features to record buying and selling activities, produce various reports, and maintain the internal date system for managing transactions.

# Install instructions
* Install Tabulate via command: pip install tabulate

## Features
Some important features:
* Feature 1
* Feature 2
* Feature 3

## Installation
1. Do this
2. Then this
3. Last thing to do

## Usage
Some examples on how to use Superpy.
1. **Add product to inventory:**

    python .\main.py buy --product_name \<name> --product_price \<price> --amount \<amount> --expiration_date \<date>

2. **Show list of inventory:**

    * <u>Total list:</u> python .\main.py report inventory
    
    * <u>Today's list (excluding expirated and sold items):</u> python main.py report inventory --now

    * <u>Yesterday's list (excluding expirated and sold items):</u> python main.py report inventory --yesterday

    * <u>Show how many items in inventory by product name:</u> python main.py report inventory --by_type

3. **Sell an item:**

    python .\main.py sell --product_name \<name> --price \<price>

    Note: you can's sell an item that's already sold.

4. **Change the date.**
    Use one of the following commands:

    * <u>Reset the date to current day:</u> python main.py reset_date
    
    * <u>Advance the day to future day:</u> python main.py --advance_time \<numbers of days>

5. **Show revenue:**
    Use one of the following commands:

    * <u>Today's revenue</u> python main.py report revenue --today

    * <u>Yesterday's revenue</u> python main.py report revenue --yesterday

    * <u>Revenue from specific date</u> python main.py report revenue --date \<date_format: YYYY-MM-DD>

## Data storage
The files where all the data is stored:
| File name | Columns |
| ----------- | ----------- |
| bought.csv | id, product_name, buy_date, buy_price, expiration_date |
| sold.cxv | id, ....
| current_day.txt | Day |
| id.txt | id |

# Author
Michel