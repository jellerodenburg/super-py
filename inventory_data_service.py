from csv_service import get_products_from_bought_csv, get_sales_from_sold_csv


def get_inventory():
    bought_products = get_products_from_bought_csv()
    ids_of_sold_products = get_ids_of_sold_products()
    inventory = []
    for product in bought_products:
        if product.id not in ids_of_sold_products:
            inventory.append(product)
    return inventory


def get_ids_of_sold_products():
    sales = get_sales_from_sold_csv()
    ids_of_sold_products = []
    for sale in sales:
        ids_of_sold_products.append(sale.bought_id)
    return ids_of_sold_products
