def can_purchase(budget: float, price: float) -> bool:
    return budget >= price

budget = 20.0
price = 2.0
can_buy = can_purchase(budget, price)
print(f"Can buy? {can_buy}")