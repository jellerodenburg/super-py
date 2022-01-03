import argparse

argparser = argparse.ArgumentParser(
    description="Supermarket inventory and sales reporting application"
)
argparser.add_argument(
    "function", help="Choose between:" + "buy, sell", action="store"
)
argparser.add_argument(
    "-n", "--name", help="specify the name of a product", action="store"
)
argparser.add_argument(
    "-p",
    "--price",
    help="specify price in euros (use decimal point as seperator for cents)",
    action="store",
    type=float,
)
argparser.add_argument(
    "-e",
    "--expiration_date",
    help="specify the expiration date of a product (use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-d",
    "--date",
    help="specify a date to use with functions: setdate, pull"
    + "(use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-f",
    "--from_date",
    help="specify the starting date for a date range (use format YYYY-MM-DD)",
    action="store",
)
argparser.add_argument(
    "-t",
    "--to_date",
    help="specify the end date for a date range (use format YYYY-MM-DD)",
    action="store",
)
