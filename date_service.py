from datetime import date, datetime
from colorprint_service import prRed, prGreen


def get_date_to_use_as_current_date():
    file = open("resources/current_date.txt", "r")
    date_as_string = file.read()
    # set date to today's date if current_date.txt is empty
    if date_as_string == "":
        current_date = date.today()
    else:
        current_date = datetime.strptime(date_as_string, "%Y-%m-%d").date()
    return current_date


def set_current_date(date):
    if is_correct_date(date):
        with open("resources/current_date.txt", "w") as file:
            file.write(date)

def is_correct_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d").date()
        return True
    except ValueError:
        prRed("Error: Please specify a valid date in format YYYY-MM-DD.")
        return False