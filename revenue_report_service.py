from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from revenue_data_service import *
from date_service import is_valid_date
from currency_service import *

console = Console()
table = Table()
table.add_column("From\nDate")
table.add_column("To\nDate")
table.add_column("Total\nItems\nSold", justify="right")
table.add_column("Average\nItem\nSell Price", justify="right")
table.add_column("Total\nRevenue\n(Sales)", justify="right")
table.add_column("Total\nCosts\n(Bought)", justify="right")
table.add_column("Total\nProfit", justify="right")


def generate_revenue_report(from_date, to_date):
    if both_args_valid(from_date, to_date):
        add_row_to_table(from_date, to_date)
        console.print(table)
        optional_add_more_date_ranges()


def optional_add_more_date_ranges():
    while Confirm.ask("Add results for another date range to this revenue report?"):
        new_from_date = prompt_new_date("From")
        new_to_date = prompt_new_date("To")
        add_row_to_table(new_from_date, new_to_date)
        console.print(table)


def prompt_new_date(date_type):
    valid_date = False
    while valid_date == False:
        user_input_new_date = Prompt.ask(f"Please enter another {date_type} Date")
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
    if from_date == None:
        Console.print("[red]Error: Please specify the from_date for the date range[/red]")
        args_not_none = False
    if to_date == None:
        Console.print("[red]Error: Please specify the to_date for the date range[/red]")
        args_not_none = False
    if args_not_none:
        if is_valid_date(from_date) and is_valid_date(to_date):
            return True
        else:
            return False
