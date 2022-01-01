from csv_service import *
from colorprint_service import prRed

sales = get_sales_from_sold_csv()


def get_revenue_in_euros(from_date, to_date):
    total_sales_in_euros = 0.0
    for sale in sales:
        if sale.sell_date >= from_date and sale.sell_date < to_date:
            total_sales_in_euros += float(sale.sell_price)
    return total_sales_in_euros


def get_number_of_sold_products(from_date, to_date):
    number_of_products_sold = 0
    for sale in sales:
        if sale.sell_date >= from_date and sale.sell_date < to_date:
            number_of_products_sold += 1
    return number_of_products_sold


