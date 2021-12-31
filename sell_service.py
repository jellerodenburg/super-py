from operator import attrgetter
from csv_service import *
from date_service import get_date_to_use_as_current_date
from colorprint_service import prRed, prGreen

current_date = get_date_to_use_as_current_date()
bought_products = get_products_from_bought_csv()
sales = get_sales_from_sold_csv()


def sell_product(product_to_sell_name, sell_price):
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
            and bought_product.expiration_date >= current_date
        ):
            products_available_to_sell.append(bought_product)
            print(f"product {bought_product} is available for sale")

    if len(products_available_to_sell) > 0:
        # sell product that has the lowest expiration_date first
        product_to_sell = min(
            products_available_to_sell, key=attrgetter("expiration_date")
        )
        sell_id = get_last_id_from_sold_csv() + 1
        sell_data = [sell_id, product_to_sell.id, current_date, sell_price]
        write_data_to_new_row_in_sold_csv(sell_data)
    else:
        prRed("Requested product is not available.")
