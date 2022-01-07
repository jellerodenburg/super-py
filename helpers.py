from datetime import date, datetime
from rich.console import Console
from rich.panel import Panel

console = Console(style="green")
error_console = Console(stderr=True, style="bold red")
today = date.today()


def get_date_to_use_as_current_date():
    file = open("resources/current_date.txt", "r")
    date_as_string = file.read()
    # set date to today's date if current_date.txt is empty
    if date_as_string == "":
        current_date = today
    else:
        current_date = datetime.strptime(date_as_string, "%Y-%m-%d").date()
    return current_date


def set_current_date(date):
    if date == "today" or date == "reset" or date == "local":
        with open("resources/current_date.txt", "w") as file:
            file.write("")
        console.print(
            Panel(
                "Current 'today'-date has been reset.\n"
                + "Local(operating system) date will be used from now on.\n"
                + f"Today is: {today}"
            )
        )
    else:
        if is_valid_date(date):
            with open("resources/current_date.txt", "w") as file:
                file.write(date)
            console.print(
                Panel(
                    f"Current date has been set to: {date}\n"
                    + "This will be used as 'today'-date for the program."
                )
            )


def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d").date()
        return True
    except ValueError:
        error_console.print(
            Panel("Error: Please specify a valid date in format YYYY-MM-DD.")
        )
        return False


def str_to_date(str):
    return datetime.strptime(str, "%Y-%m-%d").date()


def date_to_str(date):
    return datetime.strftime(date, "%Y-%m-%d")


def format_as_currency(amount):
    # round (float) amount to two decimals
    amount_rounded = round(amount, 2)
    # format to always show two decimals (for example: 0.5 -> 0.50)
    amount_formatted = "{:.2f}".format(amount_rounded)
    return "€ " + amount_formatted
