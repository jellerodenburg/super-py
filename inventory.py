from datetime import timedelta
from csv_service import get_products_from_bought_csv, get_sales_from_sold_csv
from helpers import (
    date_to_str,
    get_date_to_use_as_current_date,
    is_valid_date,
    str_to_date,
)
from rich_print_service import print_product_report


def generate_inventory_report(date_arg):
    # if user has provided "today", or no date argument, then use current_date
    if date_arg == "today" or date_arg == "t" or date_arg is None:
        date_arg = f"{date_to_str(get_date_to_use_as_current_date())}"
    if date_arg == "yesterday" or date_arg == "y":
        yesterday = get_date_to_use_as_current_date() - timedelta(days=1)
        date_arg = date_to_str(yesterday)
    if is_valid_date(date_arg):
        inventory = get_inventory(date_arg)
        report_title = f"Inventory as of {date_arg}"
        print_product_report(inventory, report_title)


def get_inventory(date_arg):
    if is_valid_date(date_arg):
        bought_products = get_products_from_bought_csv()
        inventory_date = str_to_date(date_arg)
        ids_of_sold_products = get_ids_of_sold_products()
        inventory = []
        for product in bought_products:
            if (
                product.id not in ids_of_sold_products
                and product.buy_date <= inventory_date
            ):
                inventory.append(product)
        return inventory


def get_ids_of_sold_products():
    sales = get_sales_from_sold_csv()
    ids_of_sold_products = []
    for sale in sales:
        ids_of_sold_products.append(sale.bought_id)
    return ids_of_sold_products
