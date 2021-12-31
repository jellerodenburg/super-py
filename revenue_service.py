from csv_service import *
from date_service import is_correct_date
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


def print_revenue_in_euros(from_date, to_date):
    all_args_ok = True
    if from_date == None:
        prRed("Error: Please specify the from_date for the date range")
        all_args_ok = False
    if to_date == None:
        prRed("Error: Please specify the to_date for the date range")
        all_args_ok = False
    if all_args_ok:
        if is_correct_date(from_date) and is_correct_date(to_date):
            total_sales_in_euros = get_revenue_in_euros(from_date, to_date)
            number_of_products_sold = get_number_of_sold_products(from_date, to_date)
            revenue_rounded_two_decimals = round(total_sales_in_euros, 2)
            revenue_formatted_two_decimals = "{:.2f}".format(
                revenue_rounded_two_decimals
            )
            print(
                f"Revenue from {from_date} to {to_date} is € {revenue_formatted_two_decimals}\n"
                + f"Number of products sold: {number_of_products_sold}"
            )
