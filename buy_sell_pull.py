from operator import attrgetter
from rich.console import Console
from model import Product
from inventory import get_inventory
from helpers import (
    date_to_str,
    str_to_date,
    is_valid_date,
    get_date_to_use_as_current_date,
    format_as_currency,
)
from csv_service import (
    get_last_id_from_csv,
    get_products_from_bought_csv,
    get_sales_from_sold_csv,
    write_data_to_new_row_in_csv_document,
    bought_csv,
    sold_csv,
)
from rich_print_service import (
    print_product_in_table_format,
    print_product_report,
    print_info_panel,
    print_error_panel,
    print_success_panel,
    print_warning_panel,
)

console = Console()

current_date = get_date_to_use_as_current_date()
bought_products = get_products_from_bought_csv()
sales = get_sales_from_sold_csv()


def buy_product(product_name, product_price, product_expiration_date):
    if all_buy_args_entered(
        product_name, product_price, product_expiration_date
    ):
        if is_valid_date(product_expiration_date):
            product_expiration_date = str_to_date(product_expiration_date)
            product_id = get_last_id_from_csv(bought_csv) + 1
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
            print_success_panel(
                f"Product '{product_name}' "
                + f"added with id {product_id} "
                + "to list of bought products."
            )


def all_buy_args_entered(product_name, product_price, product_expiration_date):
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


def pull_products_with_date_equal_to_or_earlier_then(date_as_string):
    date = str_to_date(date_as_string)
    current_date_string = date_to_str(current_date)
    inventory = get_inventory(current_date_string)
    pulled_products = []
    pulled_products_buy_price_total = 0.0
    print_info_panel(
        f"Searching inventory of {current_date_string} for products"
        + f" with expiration date of {date_as_string} or earlier ..."
    )
    for product in inventory:
        if product.expiration_date <= date:
            # put products in sold.csv with sell_price of 0
            sell_product(product, 0)
            pulled_products.append(product)
            pulled_products_buy_price_total += float(product.buy_price)
    if len(pulled_products) == 0:
        print_warning_panel(
            "No products found with expiration date of "
            + f"{date_as_string} or earlier"
        )
    else:
        report_title = "Pulled products"
        print_product_report(pulled_products, report_title)
        print_success_panel(
            f"Number of products pulled: {len(pulled_products)}\n"
            + "Total costs for pulled products: "
            + f"{format_as_currency(pulled_products_buy_price_total)}"
        )


def sell_product_by_name(product_name, sell_price):
    products_available_to_sell = get_products_available_for_sale(product_name)
    product_to_sell = find_product_to_sell_first(products_available_to_sell)
    if product_to_sell is None:
        print_error_panel(f"No '{product_name}' items available for sale.")
    else:
        number_of_same_products_left = len(products_available_to_sell) - 1
        sell_product(product_to_sell, sell_price)
        print_product_in_table_format(product_to_sell)
        print_success_panel(
            f"Product '{product_name}' with id {product_to_sell.id} "
            + f"sold for {format_as_currency(sell_price)} on {current_date}"
        )
        print_info_panel(
            f"Number of available '{product_name}' items left is now: "
            + f"{number_of_same_products_left}",
        )


def sell_product(product, price):
    new_sale_id = get_last_id_from_csv(sold_csv) + 1
    sell_data = [new_sale_id, product.id, current_date, price]
    write_data_to_new_row_in_csv_document(sell_data, sold_csv)


def find_product_to_sell_first(products_available_to_sell):
    if len(products_available_to_sell) > 0:
        # find product that has the lowest expiration_date
        product_to_sell = min(
            products_available_to_sell, key=attrgetter("expiration_date")
        )
        return product_to_sell
    else:
        return None


def get_products_available_for_sale(product_to_sell_name):
    products_available_to_sell = []
    products_with_desired_name = get_bought_products_by_name(
        product_to_sell_name
    )
    ids_of_sold_products = get_ids_of_sold_products()
    for bought_product in products_with_desired_name:
        if (
            bought_product.id not in ids_of_sold_products
            and bought_product.expiration_date >= current_date
        ):
            products_available_to_sell.append(bought_product)
    return products_available_to_sell


def get_ids_of_sold_products():
    ids_of_sold_products = []
    for sale in sales:
        ids_of_sold_products.append(sale.bought_id)
    return ids_of_sold_products


def get_bought_products_by_name(product_to_sell_name):
    bought_products_with_desired_name = []
    for bought_product in bought_products:
        if bought_product.name == product_to_sell_name:
            bought_products_with_desired_name.append(bought_product)
    return bought_products_with_desired_name
