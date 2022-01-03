from rich.console import Console
from model import Product
from date_service import str_to_date, is_valid_date
from csv_service import (
    get_last_id_from_bought_csv,
    write_data_to_new_row_in_csv_document,
    bought_csv,
)
from date_service import get_date_to_use_as_current_date
from rich_print_service import print_product_in_table_format

console = Console()
error_console = Console(stderr=True, style="bold red")

current_date = get_date_to_use_as_current_date()


def buy_product(product_name, product_price, product_expiration_date):
    if all_args_entered(product_name, product_price, product_expiration_date):
        if is_valid_date(product_expiration_date):
            product_expiration_date = str_to_date(product_expiration_date)
            product_id = get_last_id_from_bought_csv() + 1
            product_data = [
                product_id,
                product_name,
                current_date,
                product_price,
                product_expiration_date,
            ]
            write_data_to_new_row_in_csv_document(product_data, bought_csv)
            added_product = Product(
                product_id,
                product_name,
                current_date,
                product_price,
                product_expiration_date,
            )
            print_product_in_table_format(added_product)
            console.print("Item added succesfully to list of bought products.")


def all_args_entered(product_name, product_price, product_expiration_date):
    args_not_none = True
    if product_expiration_date is None:
        error_console.print(
            "Error: Please specify the expiration_date for the product"
        )
        args_not_none = False
    if product_name is None:
        error_console.print("Error: Please specify the name of the product")
        args_not_none = False
    if product_price is None:
        error_console.print("Error: Please specify a price for the product")
        args_not_none is False
    if product_price < 0:
        error_console.print("Error: Product price cannot be a negative amount")
        args_not_none = False
    return args_not_none
