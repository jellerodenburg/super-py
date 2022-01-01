from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from revenue_data_service import *
from date_service import is_valid_date

console = Console()
table = Table()
table.add_column("From\nDate")
table.add_column("To\nDate")
table.add_column("Total\nItems\nSold", justify="right")
table.add_column("Average\nItem Sell\nPrice", justify="right")
table.add_column("Total\nRevenue", justify="right")


def generate_revenue_report(from_date, to_date):
    if both_args_valid(from_date, to_date):
        add_row_to_table(from_date, to_date)
        console.print(table)
        optional_add_more_date_ranges()


def optional_add_more_date_ranges():
    while Confirm.ask("Add another date range to report?"):
        valid_new_from_date = False
        while valid_new_from_date == False:
            user_input_new_from_date = Prompt.ask("Please enter another From Date")
            if is_valid_date(user_input_new_from_date):
                valid_new_from_date = True
                new_validated_from_date = user_input_new_from_date
                valid_new_to_date = False
                while valid_new_to_date == False:
                    user_input_new_to_date = Prompt.ask("Please enter another To Date")
                    if is_valid_date(user_input_new_to_date):
                        valid_new_to_date = True
                        new_validated_to_date = user_input_new_to_date
                        add_row_to_table(new_validated_from_date, new_validated_to_date)
                        console.print(table)

def add_row_to_table(from_date, to_date):
    number_of_products_sold = get_number_of_sold_products(from_date, to_date)
    total_revenue = get_revenue_in_euros(from_date, to_date)
    average_item_price = 0
    if number_of_products_sold != 0:
        average_item_price = total_revenue / number_of_products_sold
    table.add_row(
        from_date,
        to_date,
        str(number_of_products_sold),
        format_as_currency(average_item_price),
        format_as_currency(total_revenue),
    )


def both_args_valid(from_date, to_date):
    args_not_none = True
    if from_date == None:
        prRed("Error: Please specify the from_date for the date range")
        args_not_none = False
    if to_date == None:
        prRed("Error: Please specify the to_date for the date range")
        args_not_none = False
    if args_not_none:
        if is_valid_date(from_date) and is_valid_date(to_date):
            return True
        else:
            return False


def format_as_currency(amount):
    amount_rounded_two_decimals = round(amount, 2)
    amount_formatted_two_decimals = "{:.2f}".format(amount_rounded_two_decimals)
    return "€ " + amount_formatted_two_decimals
