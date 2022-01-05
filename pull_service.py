from inventory_data_service import get_inventory
from currency_service import format_as_currency
from date_service import (
    str_to_date,
    get_date_to_use_as_current_date,
    date_to_str,
)
from sell_service import sell_product
from rich_print_service import (
    print_product_report,
    print_success_panel,
    print_warning_panel,
    print_info_panel,
)
from rich.console import Console

console = Console()


def pull_products_with_date_equal_to_or_earlier_then(date_as_string):
    date = str_to_date(date_as_string)
    current_date_string = date_to_str(get_date_to_use_as_current_date())
    inventory = get_inventory(current_date_string)
    pulled_products = []
    pulled_products_buy_price_total = 0.0
    print_info_panel(
        f"Searching inventory of {current_date_string} for products"
        + f" with expiration date of {date_as_string} or earlier ..."
    )
    for product in inventory:
        if product.expiration_date <= date:
            # put products in sold.csv with sell_price of 0
            sell_product(product, 0)
            pulled_products.append(product)
            pulled_products_buy_price_total += float(product.buy_price)
    if len(pulled_products) == 0:
        print_warning_panel(
            "No products found with expiration date of "
            + f"{date_as_string} or earlier"
        )
    else:
        report_title = "Pulled products"
        print_product_report(pulled_products, report_title)
        print_success_panel(
            f"Number of products pulled: {len(pulled_products)}\n"
            + "Total costs for pulled products: "
            + f"{format_as_currency(pulled_products_buy_price_total)}"
        )
