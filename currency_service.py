def format_as_currency(amount):
    amount_rounded_two_decimals = round(amount, 2)
    amount_formatted_two_decimals = "{:.2f}".format(amount_rounded_two_decimals)
    return "€ " + amount_formatted_two_decimals
