import json


with open('goods_data.json') as file:
    goods=json.load(file)


def find_average_price(goods):
    unique_goods = list(set(map(lambda good: good['name'], goods)))
    goods_prices_and_count = {good: {'price': 0, 'count': 0} for good in unique_goods}
    for good in goods:
        goods_prices_and_count[good['name']]['price'] += good['price']
        goods_prices_and_count[good['name']]['count'] += 1
    return {good: good_info['price'] / good_info['count'] for good, good_info in goods_prices_and_count.items()}

def max_average_value(goods):
    avg_prices = find_average_price(goods)
    max_avg_price = max([avg_price for avg_price in avg_prices.values()])
    return max_avg_price

# goods = [{'name': 'milk', 'price': 21.5}, {'name': 'bread', 'price': 13.5}, {'name': 'milk', 'price': 25.4},
#          {'name': 'bread', 'price': 15.6}, {'name': 'apples', 'price': 12.0}]
print("Average prices: ",find_average_price(goods))
print("The highest price: ", max_average_value(goods))



# output sample:
# Average prices:  {'apples': 12.0, 'bread': 14.55, 'milk': 23.45}
# The highest price:  23.45