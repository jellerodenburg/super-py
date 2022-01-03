from inventory_data_service import get_inventory
from date_service import str_to_date
from sell_service import sell_product
from rich_print_service import print_inventory_report
from rich.console import Console

console = Console()


def pull_products_with_date_equal_to_or_earlier_then(date_as_string):
    date = str_to_date(date_as_string)
    inventory = get_inventory()
    pulled_products = []
    for product in inventory:
        if product.expiration_date <= date:
            # puts products in sold.csv with sell_price of 0
            sell_product(product, 0)
            pulled_products.append(product)
    print_inventory_report(pulled_products)
    console.print(
        f"{len(pulled_products)} products",
        f"with expiration date {date_as_string} or earlier were pulled",
    )
