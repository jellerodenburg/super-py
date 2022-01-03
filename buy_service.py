from rich.console import Console
from model import Product
from date_service import str_to_date, is_valid_date
from csv_service import (
    get_last_id_from_bought_csv,
    write_data_to_new_row_in_csv_document,
    bought_csv,
)
from date_service import get_date_to_use_as_current_date
from rich_print_service import (
    print_product_in_table_format,
    print_error_panel,
    print_succes_panel,
)

console = Console()

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
            print_succes_panel(
                f"Product '{product_name}' with id {product_id} "
                + "added succesfully to list of bought products."
            )


def all_args_entered(product_name, product_price, product_expiration_date):
    args_not_none = True
    if product_expiration_date is None:
        print_error_panel("Error: expiration date not specified")
        args_not_none = False
    if product_name is None:
        print_error_panel("Error: name of the product not specified")
        args_not_none = False
    if product_price is None:
        print_error_panel("Error: price not specified")
        args_not_none = False
    if product_price and product_price < 0:
        print_error_panel("Error: price cannot be a negative amount")
        args_not_none = False
    return args_not_none
