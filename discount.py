def apply_discount(price):
    if price > 1500:
        return price * 0.9   # 10% discount
    else:
        return price