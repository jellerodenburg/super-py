import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from helpers import (
    is_valid_date,
    str_to_date,
    format_as_currency,
    round_and_format_two_decimals,
)
from rich_print_service import (
    print_error_panel,
    print_prompt_panel,
    print_success_panel,
)
from csv_service import (
    get_sales_from_sold_csv,
    get_products_from_bought_csv,
    write_data_to_new_row_in_csv_document,
)

console = Console()

table = Table()
table.add_column("From\nDate")
table.add_column("To\nDate\n(excl.)")
table.add_column("Items\nSold", justify="right")
table.add_column("Item\nSell Price\nAverage", justify="right")
table.add_column("Revenue\n(Sales)", justify="right")
table.add_column("Total\nCosts\n(Buy)", justify="right")
table.add_column("Profit\n(Revenue - Costs)", justify="right")

sales_report_csv_data = [
    [
        "From Date",
        "To Date",
        "Items Sold",
        "Item Sell Price Average",
        "Revenue (Sales)",
        "Total Costs (Buy)",
        "Profit (Revenue - Costs)",
    ]
]


def generate_sales_report(from_date, to_date):
    if both_args_valid(from_date, to_date):
        add_row_to_report(from_date, to_date)
        console.print(table)
        optional_add_more_date_ranges()
    optional_write_sales_report_to_csv()


def optional_add_more_date_ranges():
    add_more = True
    while add_more is True:
        print_prompt_panel(
            "Add results for another date range ton sales report?"
        )
        add_more = Confirm.ask()
        if add_more:
            new_from_date = prompt_new_date("From")
            new_to_date = prompt_new_date("To")
            add_row_to_report(new_from_date, new_to_date)
            console.print(table)


def prompt_new_date(date_type):
    valid_date = False
    while valid_date is False:
        print_prompt_panel(f"Please enter another {date_type} Date:")
        user_input_new_date = Prompt.ask()
        if is_valid_date(user_input_new_date):
            valid_date = True
            return user_input_new_date


def add_row_to_report(from_date, to_date):
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
    sales_report_csv_data.append(
        [
            from_date,
            to_date,
            str(number_of_products_sold),
            round_and_format_two_decimals(average_item_price),
            round_and_format_two_decimals(revenue),
            round_and_format_two_decimals(costs_of_products),
            round_and_format_two_decimals(profit),
        ]
    )


def optional_write_sales_report_to_csv():
    print_prompt_panel("Export sales report data to .csv file?")
    if Confirm.ask():
        file_name_ok = False
        while file_name_ok is False:
            path_and_file_name = prompt_export_file_name()
            # try to create file, if file does not exist yet: create file
            try:
                open(path_and_file_name, "x")
                file_name_ok = True
            # if file name already exists: ask to overwrite or prompt new name
            except FileExistsError:
                print_error_panel("File already exists! Overwrite?")
                confirm_overwrite = Confirm.ask()
                if confirm_overwrite:
                    # overwrite file
                    open(path_and_file_name, "w")
                    file_name_ok = True
                else:
                    file_name_ok = False
        for row in sales_report_csv_data:
            write_data_to_new_row_in_csv_document(row, path_and_file_name)
        print_success_panel(f"File saved as: '{path_and_file_name}'")


def prompt_export_file_name():
    print_prompt_panel(
        "CSV file will be saved to directory: 'csv_exports'\n"
        + "Please enter a name for your file:"
    )
    user_input_file_name = Prompt.ask()
    user_input_file_name.strip()
    if not user_input_file_name.endswith(".csv"):
        user_input_file_name += ".csv"
    save_path = "csv_exports"
    path_and_file_name = os.path.join(save_path, user_input_file_name)
    return path_and_file_name


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
