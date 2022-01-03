def format_as_currency(amount):
    # round (float) amount to two decimals
    amount_rounded = round(amount, 2)
    # format to always show two decimals (for example: 0.5 -> 0.50)
    amount_formatted = "{:.2f}".format(amount_rounded)
    return "€ " + amount_formatted
