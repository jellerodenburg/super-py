from csv_service import get_products_from_bought_csv, get_sales_from_sold_csv
from date_service import (
    date_to_str,
    str_to_date,
    is_valid_date,
    get_date_to_use_as_current_date,
)


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
