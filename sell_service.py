from operator import attrgetter
from csv_service import *
from date_service import get_date_to_use_as_current_date
from colorprint_service import prRed, prGreen
from currency_service import *
from rich import print

current_date = get_date_to_use_as_current_date()
bought_products = get_products_from_bought_csv()
sales = get_sales_from_sold_csv()


def sell_product(product_name, sell_price):
    products_available_to_sell = get_products_available_for_sale(product_name)
    product_to_sell = find_product_to_sell_first(products_available_to_sell)
    if product_to_sell == None:
        prRed("Requested product is not available.")
    else:
        number_of_same_products_left = len(products_available_to_sell) - 1
        new_sale_id = get_last_id_from_sold_csv() + 1
        sell_data = [new_sale_id, product_to_sell.id, current_date, sell_price]
        write_data_to_new_row_in_csv_document(sell_data, sold_csv)
        print(f"[blue]{product_to_sell}[/blue]")
        print(f"Sold for {format_as_currency(sell_price)}")
        print(f"Number of available '{product_name}' items left: {number_of_same_products_left}")


def find_product_to_sell_first(products_available_to_sell):
    if len(products_available_to_sell) > 0:
        # find product that has the lowest expiration_date
        product_to_sell = min(
            products_available_to_sell, key=attrgetter("expiration_date")
        )
        return product_to_sell
    else: return None

def get_products_available_for_sale(product_to_sell_name):
    products_available_to_sell = []
    products_with_desired_name = get_bought_products_by_name(product_to_sell_name)
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
