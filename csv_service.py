import csv
from datetime import datetime
from date_service import str_to_date
from model import Product, Sale
from rich.console import Console
from rich_print_service import print_error_panel
import sys

console = Console()
error_console = Console(stderr=True, style="bold red")

sold_csv = "resources/sold.csv"
bought_csv = "resources/bought.csv"


def get_sales_from_sold_csv():
    sales = []
    with open("resources/sold.csv", "r", encoding="UTF8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sale = Sale(
                row["id"],
                row["bought_id"],
                datetime.strptime(row["sell_date"], "%Y-%m-%d").date(),
                row["sell_price"],
            )
            sales.append(sale)
    return sales


def get_products_from_bought_csv():
    products = []
    with open("resources/bought.csv", "r", encoding="UTF8") as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            count += 1
            try:
                product = Product(
                    row["id"],
                    row["product_name"],
                    str_to_date(row["buy_date"]),
                    row["buy_price"],
                    str_to_date(row["expiration_date"]),
                )
            except Exception:
                print_error_panel(
                    "Unable to complete your request:\n"
                    + f"Error in bought.csv on line: {count +1}"
                    + "\nExiting program"
                )
                sys.exit()
            products.append(product)
    return products


def write_data_to_new_row_in_csv_document(data, document_path):
    with open(document_path, "a", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()


def get_last_id_from_bought_csv():
    with open("resources/bought.csv", "r", encoding="UTF8") as file:
        opened_file = file.readlines()
        first_value_of_last_row = opened_file[-1].split(",")[0]
        if first_value_of_last_row == "id":
            last_id = 0
        else:
            last_id = int(first_value_of_last_row)
    return last_id


def get_last_id_from_sold_csv():
    with open("resources/sold.csv", "r", encoding="UTF8") as file:
        opened_file = file.readlines()
        first_value_of_last_row = opened_file[-1].split(",")[0]
        if first_value_of_last_row == "id":
            last_id = 0
        else:
            last_id = int(first_value_of_last_row)
    return last_id
