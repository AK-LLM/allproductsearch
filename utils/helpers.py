def clean_price(price_str):
    """Standardizes price formats, removes extraneous chars."""
    if not price_str:
        return ""
    price = price_str.replace("$", "").replace(",", "").split()[0]
    try:
        price_val = float(price)
        return f"${price_val:,.2f}"
    except Exception:
        return price_str.strip()
