from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from helpers import is_valid_date, str_to_date, format_as_currency
from rich_print_service import print_error_panel
from csv_service import get_sales_from_sold_csv, get_products_from_bought_csv

console = Console()
table = Table()
table.add_column("From\nDate")
table.add_column("To\nDate\n(excl.)")
table.add_column("Items\nSold", justify="right")
table.add_column("Item\nSell Price\nAverage", justify="right")
table.add_column("Revenue\n(Sales)", justify="right")
table.add_column("Total\nCosts\n(Buy)", justify="right")
table.add_column("Profit\n(Revenue - Costs)", justify="right")


def generate_sales_report(from_date, to_date):
    if both_args_valid(from_date, to_date):
        add_row_to_table(from_date, to_date)
        console.print(table)
        optional_add_more_date_ranges()


def optional_add_more_date_ranges():
    while Confirm.ask(
        "Add results for another date range to this revenue report?"
    ):
        new_from_date = prompt_new_date("From")
        new_to_date = prompt_new_date("To")
        add_row_to_table(new_from_date, new_to_date)
        console.print(table)


def prompt_new_date(date_type):
    valid_date = False
    while valid_date is False:
        user_input_new_date = Prompt.ask(
            f"Please enter another {date_type} Date"
        )
        if is_valid_date(user_input_new_date):
            valid_date = True
            return user_input_new_date


def add_row_to_table(from_date, to_date):
    number_of_products_sold = get_number_of_sold_products(from_date, to_date)
    revenue = get_revenue_in_euros(from_date, to_date)
    costs_of_products = get_costs_of_bought_products(from_date, to_date)
    profit = revenue - costs_of_products
    average_item_price = 0
    if number_of_products_sold != 0:
        average_item_price = revenue / number_of_products_sold
    table.add_row(
        from_date,
        to_date,
        str(number_of_products_sold),
        format_as_currency(average_item_price),
        format_as_currency(revenue),
        format_as_currency(costs_of_products),
        format_as_currency(profit),
    )


def both_args_valid(from_date, to_date):
    args_not_none = True
    if from_date is None:
        print_error_panel(
            "[red]Error: Please specify the from_date for the date range[/red]"
        )
        args_not_none = False
    if to_date is None:
        print_error_panel(
            "[red]Error: Please specify the to_date for the date range[/red]"
        )
        args_not_none = False
    if args_not_none:
        if is_valid_date(from_date) and is_valid_date(to_date):
            return True
        else:
            return False


sales = get_sales_from_sold_csv()


def get_number_of_sold_products(from_date, to_date):
    from_date = str_to_date(from_date)
    to_date = str_to_date(to_date)
    number_of_products_sold = 0
    for sale in sales:
        if sale.sell_date >= from_date and sale.sell_date < to_date:
            number_of_products_sold += 1
    return number_of_products_sold


def get_revenue_in_euros(from_date, to_date):
    from_date = str_to_date(from_date)
    to_date = str_to_date(to_date)
    revenue_in_euros = 0.0
    for sale in sales:
        if sale.sell_date >= from_date and sale.sell_date < to_date:
            revenue_in_euros += float(sale.sell_price)
    return revenue_in_euros


def get_costs_of_bought_products(from_date, to_date):
    from_date = str_to_date(from_date)
    to_date = str_to_date(to_date)
    bought_products = get_products_from_bought_csv()
    costs_of_products = 0.0
    for product in bought_products:
        if product.buy_date >= from_date and product.buy_date < to_date:
            costs_of_products += float(product.buy_price)
    return costs_of_products
