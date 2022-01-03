from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from currency_service import format_as_currency
from date_service import date_to_str, get_date_to_use_as_current_date
from datetime import timedelta

console = Console()
error_console = Console(stderr=True, style="bold red")


def print_product_in_table_format(product):
    table = Table(box=box.SIMPLE)
    table.add_column("Product", justify="right")
    table.add_column(product.name, justify="left")

    id = str(product.id)
    buy_date = date_to_str(product.buy_date)
    buy_price = format_as_currency(float(product.buy_price))
    expiration_date = date_to_str(product.expiration_date)
    table.add_row("id:", id)
    table.add_row("buy date:", buy_date)
    table.add_row("buy price:", buy_price)
    table.add_row("exp. date:", expiration_date)
    console.print(Panel(table))


def print_inventory_report(inventory):
    current_date = get_date_to_use_as_current_date()

    table = Table()
    table.add_column("Id")
    table.add_column("Name")
    table.add_column("Buy Date")
    table.add_column("Buy Price")
    table.add_column("Exp. Date")

    for product in inventory:
        id = str(product.id)
        buy_date = date_to_str(product.buy_date)
        buy_price = format_as_currency(float(product.buy_price))
        expiration_date = date_to_str(product.expiration_date)
        if product.expiration_date < current_date:
            expiration_date = f"{expiration_date} [b red]Expired![/b red]"
        elif product.expiration_date == current_date:
            expiration_date = (
                f"{expiration_date}[dark_orange]  Today![/dark_orange]"
            )
        elif product.expiration_date == current_date + timedelta(days=1):
            expiration_date = f"{expiration_date}[gold1] Tomorrow![/gold1]"
        else:
            expiration_date = date_to_str(product.expiration_date)
        table.add_row(
            id,
            product.name,
            buy_date,
            buy_price,
            expiration_date,
        )

    console.print(Panel.fit(table))


def print_error_panel(string):
    error_console.print(Panel(string))


def print_succes_panel(string):
    console.print(Panel(string, style="green"))


def print_info_panel(string):
    console.print(Panel(string, style="blue"))
