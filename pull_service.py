from inventory_data_service import get_inventory
from date_service import (
    str_to_date,
    get_date_to_use_as_current_date,
    date_to_str,
)
from sell_service import sell_product
from rich_print_service import (
    print_product_report,
    print_succes_panel,
    print_warning_panel,
)
from rich.console import Console

console = Console()


def pull_products_with_date_equal_to_or_earlier_then(date_as_string):
    date = str_to_date(date_as_string)
    inventory = get_inventory(date_to_str(get_date_to_use_as_current_date()))
    pulled_products = []
    for product in inventory:
        if product.expiration_date <= date:
            # puts products in sold.csv with sell_price of 0
            sell_product(product, 0)
            pulled_products.append(product)
    if len(pulled_products) == 0:
        print_warning_panel(
            "No products found with expiration date of "
            + f"{date_as_string} or earlier"
        )
    else:
        report_title = "Pulled products"
        print_product_report(pulled_products, report_title)
        print_succes_panel(
            f"{len(pulled_products)} products "
            + f"with expiration date {date_as_string} or earlier were pulled",
        )
