# Imports
import argparse
import sys
import csv
import os
import pathlib
import pandas
from os import path
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# check if bought.csv exists, create it if it doesn't
if not os.path.isfile('bought.csv'):
    with open('bought.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date'])
if not os.path.isfile('sold.csv'):
    with open('sold.csv', 'w', newline='') as g:
        writer = csv.writer(g)
        writer.writerow(["id", "product_name", "bought_id", "sell_date", "sell_price"])

# open bought.csv and sold.csv files
bought = open("bought.csv", "a", newline="")
sold = open("sold.csv", "a", newline="")
writer = csv.writer(bought)
bought.close()
sold.close()

def get_bought_id(product_name):
    """
    Given a product name, this function reads the 'bought.csv' file and looks for
    a row that matches the product name. If found, it returns the ID of that row.
    If not found, it returns the string 'OUT OF STOCK!'.
    """
    with open("bought.csv", "r", newline="") as bought:
        reader = csv.DictReader(bought)
        for row in reader:
            if row["product_name"] == product_name:
                return row["id"]
        return "OUT OF STOCK!"


def main():
    parser = argparse.ArgumentParser(description="Welcome to the inventory system")
    parser.add_argument("option", 
                        type=str,
                        nargs=1,
                        choices= ["buy", "sell"],
                        
                        help="Buying or selling?")
    parser.add_argument("-p", "--product-name",
                        type=str,
                         
                        required=True,
                        dest="product",
                        help="Name of the product")
    parser.add_argument("-d", "--buy-date",
                        type=str,
                        dest="date",
                        help="Date when bought")
    parser.add_argument("--price", 
                        type=float,
                        dest="price", 
                        help="Buying price of the product")
    parser.add_argument("-e", "--expiration",
                        type=str,
                        dest="expiration",
                        help="Expiration date of the product")
    parser.add_argument("-s", "--sell_date",
                        type=str,
                        dest="sell_date",
                        help="Date of selling")
    parser.add_argument("--sell-price",
                        type=str,
                        dest="sell_price",
                        help="Selling price of the product") 
    #parser.add_argument("--advance-time",
                        
                        
    
    parsed_args = parser.parse_args()

    if parsed_args.option[0] == "buy":
        # Create bought.csv file if it doesn't exist
        if not os.path.exists("bought.csv"):
            with open("bought.csv", "w", newline="") as bought:
                writer = csv.writer(bought)
                writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])

        # Get the next ID for the new row
        with open("bought.csv", "r", newline="") as bought:
            reader = csv.reader(bought)
            next_id = str(sum(1 for row in reader))

        # Add the new row to the file
        with open("bought.csv", "a", newline="") as bought:
            writer = csv.writer(bought)
            writer.writerow([next_id, parsed_args.product, parsed_args.date, parsed_args.price, parsed_args.expiration])
            print(f"Bought {parsed_args.product} on {parsed_args.date} for {parsed_args.price} with expiration date {parsed_args.expiration} added to inventory")
    
    elif parsed_args.option[0] == "sell":
        product_name = parsed_args.product
        bought_id = get_bought_id(product_name)
        if bought_id == "OUT OF STOCK!":
            print(f"{product_name} is out of stock!")
        else:
            if not os.path.exists("sold.csv"):
                with open ("sold.csv", "a", newline="") as sold:
                    writer = csv.writer(sold)
                    writer.writerow(["id", "product_name", "bought_id", "sell_date", "sell_price"])
            with open("sold.csv", "r", newline="") as sold:
                    reader = csv.reader(sold)
                    next_id = str(sum(1 for row in reader))
            with open("sold.csv", "a", newline="") as sold:
                    writer = csv.writer(sold)
                    writer.writerow([next_id, product_name, bought_id, parsed_args.sell_date, parsed_args.sell_price]) 
                    print(f"sold {product_name} for {parsed_args.sell_price}")
    return

if __name__ == "__main__":
    main()
