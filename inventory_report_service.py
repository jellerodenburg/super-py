from datetime import timedelta
from inventory_data_service import get_inventory
from rich_print_service import print_product_report
from date_service import (
    get_date_to_use_as_current_date,
    date_to_str,
    is_valid_date,
)


def generate_inventory_report(date_arg):
    # if user has provided "today", or no date argument, then use current_date
    if date_arg == "today" or date_arg == "t" or date_arg is None:
        date_arg = f"{date_to_str(get_date_to_use_as_current_date())}"
    if date_arg == "yesterday" or date_arg == "y":
        yesterday = get_date_to_use_as_current_date() - timedelta(days=1)
        date_arg = date_to_str(yesterday)
    if is_valid_date(date_arg):
        inventory = get_inventory(date_arg)
        report_title = f"Inventory as of {date_arg}"
        print_product_report(inventory, report_title)
