from rich.console import Console
from rich.table import Table
from datetime import datetime
from currency_service import *

console = Console()


def print_product_table_format(product):
    table = Table()

    table.add_column("Item name: ", justify="right")
    table.add_column(product.name, justify="left")

    id = str(product.id)
    buy_date = datetime.strftime(product.buy_date, "%Y-%m-%d")
    buy_price = format_as_currency(float(product.buy_price))
    expiration_date = datetime.strftime(product.expiration_date, "%Y-%m-%d")

    table.add_row("id: ", id)
    table.add_row("buy date: ", buy_date)
    table.add_row("buy price: ", buy_price)
    table.add_row("exp. date: ", expiration_date)

    console.print(table)
