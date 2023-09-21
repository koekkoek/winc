# SuperPy
SuperPy is a command-line based inventory management tool designed to keep track of supermarket products. It provides features to record buying and selling activities, produce various reports, and maintain the internal date system for managing transactions.

# Install instructions

1. Make sure you have the latest Python version installed.
2. Download all files to your computer
3. Before running the application, instal the following modules:
    * Install Rich via command: pip install rich
    * Install Tabulate via command: pip install tabulate
4. You can start using the program in your command line interface.

## Features and usage tips
Some examples on how to use Superpy.
1. **Want to try super.py with demo data? Use:**

    python super.py import

2. **Add product to inventory:**

    python super.py buy --product_name \<name> --product_price \<price> --expiration_date \<date>

3. **Show list of inventory:**

    Use one of the following commands:

    * <u>Total list:</u> python super.py report inventory
    
    * <u>Today's list (excluding expirated and sold items)</u>: python super.py report inventory --now
    
            Want to export today's report list in a CSV file? Use python super.py report inventory --now --export
            Want to export today's report list in a JSON file? Use python super.py report inventory --now --export_json 

    * <u>Yesterday's list (excluding expirated and sold items)</u>: python super.py report inventory --yesterday
            
            Want to export yesterday's report list in a CSV file? Use python super.py report inventory --yesterday --export
            Want to export yesterday's report list in a JSON file? Use python super.py report inventory --yesterday --export_json

    * <u>Show how many items in inventory by product name</u>: python super.py report inventory --by_type

4. **Sell an item:**

    python super.py sell --product_name \<name> --price \<price>

    Note: you can's sell an item that's already sold.

5. **Change the date.**
    
    Use one of the following commands:

    * <u>Reset the date to current day</u>: python super.py set_date \<date_format: YYYY-MM-DD>
    
    * <u>Advance the day to future day</u>: python super.py advance_time \<numbers of days>

6. **Show revenue:**
    
    Use one of the following commands:

    * <u>Today's revenue</u>: python super.py report revenue --today

    * <u>Yesterday's revenue</u>: python super.py report revenue --yesterday

    * <u>Revenue from specific date</u>: python super.py report revenue --date \<date_format: YYYY-MM-DD>

7. **Get profit report:**
    
    Use one of the following commands:

    * <u>Today's profit</u>: python super.py report profit --today

    * <u>Yesterday's profit</u>: python super.py report profit --yesterday

    * <u>Profit from specific date</u>: python super.py report profit --date \<date_format: YYYY-MM-DD>

## Data storage
The files where all the data is stored:

| File name | Columns |
| ----------- | ----------- |
| bought.csv | id, product_name, buy_date, buy_price, expiration_date |
| sold.cxv | id, bought_id, sell_date, sell_price |
| current_day.txt | Current day the computer uses |
| id.txt | Latest used ID |

# Author
Michel. Need some help? Send an e-mail to helpdesk@superpy.nl
