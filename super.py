# Imports
import argparse
from operator import attrgetter
from model import Product, Sale
from datetime import date, datetime
from colorprint_service import prRed, prGreen
from csv_service import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
today_as_string = datetime.today().strftime("%Y-%m-%d")
today_as_datetime = datetime.strptime(today_as_string, "%Y-%m-%d")


def buy_product(product_name, product_price, product_expiration_date):
    if is_correct_date(product_expiration_date):
        product_id = get_last_id_from_bought_csv() + 1
        product_data = [
            product_id,
            product_name,
            today_as_string,
            product_price,
            product_expiration_date,
        ]
        write_data_to_new_row_in_bought_csv(product_data)
        added_product = Product(
            product_id,
            product_name,
            today_as_string,
            product_price,
            product_expiration_date,
        )
        prGreen("Product succesfully added to list of bought products.")
        prGreen(added_product)


def sell_product(product_to_sell_name, sell_price):
    bought_products = get_products_from_bought_csv()
    sales = get_sales_from_sold_csv()
    bought_products_with_desired_name = []
    ids_of_sold_products = []
    products_available_to_sell = []
    for bought_product in bought_products:
        if bought_product.name == product_to_sell_name:
            bought_products_with_desired_name.append(bought_product)
    print(f"products with desire name: {bought_products_with_desired_name}")
    for sale in sales:
        ids_of_sold_products.append(sale.bought_id)
    for bought_product in bought_products_with_desired_name:
        print(f"checking product {bought_product}")
        if (
            bought_product.id not in ids_of_sold_products
            and bought_product.expiration_date >= today_as_datetime
        ):
            products_available_to_sell.append(bought_product)
            print(f"product {bought_product} is available for sale")

    if len(products_available_to_sell) > 0:
        # sell product that has the lowest expiration_date first
        product_to_sell = min(
            products_available_to_sell, key=attrgetter("expiration_date")
        )
        sell_id = get_last_id_from_sold_csv() + 1
        sell_data = [sell_id, product_to_sell.id, today_as_string, sell_price]
        write_data_to_new_row_in_sold_csv(sell_data)
    else:
        prRed("Requested product is not available.")


def is_correct_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        prRed(
            "Product not saved to inventory list.\n"
            "Please specify a correct date in format YYYY-MM-DD."
        )
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Supermarket inventory and sales reporting application"
    )
    parser.add_argument("function", help="Choose between: buy, sell", action="store")
    parser.add_argument(
        "-n", "--name", help="specify the name of a product", action="store"
    )
    parser.add_argument(
        "-p",
        "--price",
        help="specify price in euros (use decimal point as seperator for cents)",
        action="store",
        type=float,
    )
    parser.add_argument(
        "-e",
        "--expiration_date",
        help="specify the expiration date of a product (use format YYYY-MM-DD)",
        action="store",
    )
    args = parser.parse_args()
    if args.function == "buy":
        all_args_ok = True
        if args.expiration_date == None:
            prRed("Error: Please specify the expiration_date for the product")
            all_args_ok = False
        if args.name == None:
            prRed("Error: Please specify the name of the product")
            all_args_ok = False
        if args.price == None:
            prRed("Error: Please specify a price for the product")
            all_args_ok = False
        if all_args_ok:
            buy_product(args.name, args.price, args.expiration_date)
    if args.function == "sell":
        sell_product(args.name, args.price)


if __name__ == "__main__":
    main()
