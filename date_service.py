from datetime import date, datetime
from rich.console import Console
from rich_print_service import print_error_panel

error_console = Console(stderr=True, style="bold red")


def get_date_to_use_as_current_date():
    file = open("resources/current_date.txt", "r")
    date_as_string = file.read()
    # set date to today's date if current_date.txt is empty
    if date_as_string == "":
        current_date = date.today()
    else:
        current_date = str_to_date(date_as_string)
    return current_date


def set_current_date(date):
    if is_valid_date(date):
        with open("resources/current_date.txt", "w") as file:
            file.write(date)


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d").date()
        return True
    except ValueError:
        print_error_panel(
            "Error: Please specify a valid date in format YYYY-MM-DD."
        )
        return False


def str_to_date(str):
    return datetime.strptime(str, "%Y-%m-%d").date()


def date_to_str(date):
    return datetime.strftime(date, "%Y-%m-%d")
