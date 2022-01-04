# Imports
from datetime import date
from argparse_service import argparser
from buy_service import buy_product
from date_service import set_current_date, get_date_to_use_as_current_date
from pull_service import pull_products_with_date_equal_to_or_earlier_then
from revenue_report_service import generate_revenue_report
from sell_service import sell_product_by_name
from inventory_report_service import generate_inventory_report
from rich_print_service import print_warning_panel

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


def main():
    args = argparser.parse_args()
    if args.function == "buy":
        buy_product(args.name, args.price, args.expiration_date)
    if args.function == "sell":
        sell_product_by_name(args.name, args.price)
    if args.function == "setdate":
        set_current_date(args.date)
    if args.function == "revenue":
        generate_revenue_report(args.from_date, args.to_date)
    if args.function == "inventory":
        generate_inventory_report(args.date)
    if args.function == "pull":
        pull_products_with_date_equal_to_or_earlier_then(args.date)


if __name__ == "__main__":
    main()
    current_date = get_date_to_use_as_current_date()
    if current_date != date.today():
        print_warning_panel(
            f"NOTE! Current 'today'-date for super.py is set to: "
            + f"[bold]{current_date}[/bold]"
        )
