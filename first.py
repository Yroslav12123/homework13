def calculate_total(prices: list[float]) -> float:
    if not prices:
        return 0
    return sum(prices)

prices = [1, 2, 5, 50, 100]
total = calculate_total(prices)
print(total)