def solution(order):
    prices = {"latte": 5000, "americano": 4500, "anything": 4500}
    counts = {item: sum(1 for order_item in order if item in order_item) for item in prices.keys()}
    total_price = sum(counts[item] * price for item, price in prices.items())
    return total_price

