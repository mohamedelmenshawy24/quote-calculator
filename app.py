def calculate_quote(base_price, markup_percent):
    """Calculate price after adding markup."""
    if base_price < 0 or markup_percent < -100:
        raise ValueError("Invalid base price or markup")
    return base_price * (1 + markup_percent / 100)
