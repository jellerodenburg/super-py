# Imports
from datetime import date
from argparse_service import argparser
from buy_service import *
from date_service import *
from revenue_report_service import *
from sell_service import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# default current_date is today's date
# current_date can be changed with set_current_date()
current_date = date.today()


def main():
    args = argparser.parse_args()
    if args.function == "buy":
        buy_product(args.name, args.price, args.expiration_date)
    if args.function == "sell":
        sell_product(args.name, args.price)
    if args.function == "setdate":
        set_current_date(args.current_date)
    if args.function == "revenue":
        generate_revenue_report(args.from_date, args.to_date)
    


if __name__ == "__main__":
    current_date = get_date_to_use_as_current_date()
    main()
    current_date = get_date_to_use_as_current_date()
    if current_date != date.today():
        print(f"NOTE! current 'today'-date is set to: {current_date}")
