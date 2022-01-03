from rich.console import Console
from date_service import *
from csv_service import *
from date_service import get_date_to_use_as_current_date
from rich_print_service import print_product_table_format

console = Console()
error_console = Console(stderr=True, style="bold red")

current_date = get_date_to_use_as_current_date()

def buy_product(product_name, product_price, product_expiration_date):
    all_args_ok = True
    if product_expiration_date == None:
        error_console.print("Error: Please specify the expiration_date for the product")
        all_args_ok = False
    if product_name == None:
        error_console.print("Error: Please specify the name of the product")
        all_args_ok = False
    if product_price == None:
        error_console.print("Error: Please specify a price for the product")
        all_args_ok = False
    if product_price < 0:
        error_console.print("Error: Product price cannot be a negative amount")
        all_args_ok = False
    if all_args_ok:
        if is_valid_date(product_expiration_date):
            product_expiration_date = datetime.strptime(product_expiration_date, "%Y-%m-%d").date()
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
            print_product_table_format(added_product)
            console.print(f"Item added succesfully to list of bought products.")