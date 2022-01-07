from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from helpers import (
    date_to_str,
    get_date_to_use_as_current_date,
    format_as_currency,
)
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


def print_product_report(inventory, table_title):
    current_date = get_date_to_use_as_current_date()

    table = Table(title=f"{table_title}")
    table.add_column("Id", justify="right")
    table.add_column("Name")
    table.add_column("Buy Date")
    table.add_column("Buy Price", justify="right")
    table.add_column("Expiration Date")

    for product in inventory:
        id = str(product.id)
        buy_date = date_to_str(product.buy_date)
        buy_price = format_as_currency(float(product.buy_price))
        expiration_date = date_to_str(product.expiration_date)
        styled_expiration_date = style_expiration_date(
            current_date, product, expiration_date
        )
        table.add_row(
            id,
            product.name,
            buy_date,
            buy_price,
            styled_expiration_date,
        )

    console.print(Panel.fit(table))


def style_expiration_date(current_date, product, expiration_date):
    if product.expiration_date < current_date:
        expiration_date = f"[b red]{expiration_date} Expired![/b red]"
    elif product.expiration_date == current_date:
        expiration_date = f"[orange3]{expiration_date} Today![/orange3]"
    elif product.expiration_date == current_date + timedelta(days=1):
        expiration_date = f"[gold3]{expiration_date} Tomorrow![/gold3]"
    else:
        expiration_date = (
            f"[green]{date_to_str(product.expiration_date)}[/green]"
        )
    return expiration_date


def print_error_panel(string):
    error_console.print(Panel(string))


def print_success_panel(string):
    console.print(Panel(string, style="green"))


def print_info_panel(string):
    console.print(Panel(string, style="blue"))


def print_warning_panel(string):
    console.print(Panel(string, style="orange3"))


def print_setdate_warning_panel(current_date):
    print_warning_panel(
        "NOTE! Current 'today'-date for super.py is set to: "
        + f"[b]{current_date}[/b]\n"
        + "Current date can be (re)set to local operating system date"
        + " with command: [i b]setdate -d local[/i b]"
    )
