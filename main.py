from price import get_price
from discount import apply_discount

item = "shoes"

price = get_price(item)
final_price = apply_discount(price)

print("Item:", item)
print("Original Price:", price)
print("Final Price:", final_price)