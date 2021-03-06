import argparse

argparser = argparse.ArgumentParser(
    description="super.py is a supermarket inventory and sales reporting app"
)
argparser.add_argument(
    "function",
    help="options: buy, sell, pull, inventory, sales, setdate",
    action="store",
)
argparser.add_argument(
    "-d",
    "--date",
    help="date to use with functions: inventory, pull, setdate"
    + " (use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-e",
    "--expiration_date",
    help="expiration date of a product" + " (use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-f",
    "--from_date",
    help="starting date for a date range" + " (use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-n", "--name", help="name of a product", action="store"
)
argparser.add_argument(
    "-p",
    "--price",
    help="price in euros (note: use decimal point as separator for cents)",
    action="store",
    type=float,
)
argparser.add_argument(
    "-t",
    "--to_date",
    help="end date (exclusive) for a date range (use format YYYY-MM-DD)",
    action="store",
)
