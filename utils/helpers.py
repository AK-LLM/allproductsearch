def clean_price(price_str):
    if not price_str:
        return ""
    import re
    m = re.search(r"[\d,.]+", price_str.replace(",", ""))
    if m:
        return f"${m.group(0)}"
    return price_str.strip()
