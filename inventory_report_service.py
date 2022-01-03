from inventory_data_service import get_inventory
from rich_print_service import print_inventory_report


def generate_inventory_report():
    inventory = get_inventory()
    print_inventory_report(inventory)
