# 1
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}


def convert(currency_in: str, currency_out: str, number_of: int) -> float:
    return round(
        exchange_rates[currency_out] / exchange_rates[currency_in] * number_of, 2
    )
