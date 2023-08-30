# SuperPy
SuperPy is a command-line based inventory management tool designed to keep track of supermarket products. It provides features to record buying and selling activities, produce various reports, and maintain the internal date system for managing transactions.

## Features
Some important features:
* Feature 1
* Feature 2
* Feature 3

## Installation
1. Doe this
2. Then this
3. Last thing to do

## Usage
Some examples on how to use Superpy.
1. **Add product to inventory:**

    python .\main.py buy --product_name \<name> --product_price \<price> --amount \<amount> --expiration_date \<date>

2. **Show list of total inventory:**

    python .\main.py report inventory

3. **Sell an item:**

    python .\main.py sell --product_name \<name> --price \<price>

## Data storage
The files where all the data is stored:
| File name | Columns |
| ----------- | ----------- |
| bought.csv | id, product_name, buy_date, buy_price, expiration_date |
| sold.cxv | id, ....
| current_day.txt | Day |
| id.txt | id |

# Install
* Install Tabulate via command: pip install tabulate

# Author
Michel