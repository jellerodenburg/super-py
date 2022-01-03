from operator import attrgetter
from csv_service import (
    get_last_id_from_sold_csv,
    get_products_from_bought_csv,
    get_sales_from_sold_csv,
    write_data_to_new_row_in_csv_document,
    sold_csv,
)
from date_service import get_date_to_use_as_current_date
from currency_service import format_as_currency
from rich import print
from rich_print_service import print_product_in_table_format

current_date = get_date_to_use_as_current_date()
bought_products = get_products_from_bought_csv()
sales = get_sales_from_sold_csv()


def sell_product_by_name(product_name, sell_price):
    products_available_to_sell = get_products_available_for_sale(product_name)
    product_to_sell = find_product_to_sell_first(products_available_to_sell)
    if product_to_sell is None:
        print(f"[red]No '{product_name}' items available for sale.[/red]")
    else:
        number_of_same_products_left = len(products_available_to_sell) - 1
        sell_product(product_to_sell, sell_price)
        print_product_in_table_format(product_to_sell)
        print(f"Sold for {format_as_currency(sell_price)}")
        print(
            f"Number of available '{product_name}' items left:",
            f"{number_of_same_products_left}",
        )


def sell_product(product, price):
    new_sale_id = get_last_id_from_sold_csv() + 1
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
