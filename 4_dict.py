# 12.	Задано інформацію про   автомобілей (модель, вартість, максимальна швидкість). 
# Вивести назви автомобілів, у яких максимальна швидкість перевищує 180 км за годину. 
# Знайти найдешевший автомобіль.

import json


with open('cars_data.json') as file:
    cars=json.load(file)

print("Cars dataset:")
for car in cars:
    print(car)

print("Cars with maximum speed larger than 180:")
for car in cars:
    if int(car.get("speed"))>180:
        print(car.get("model"))



min_price=int(cars[0].get("price"))
for car in cars:
    if int(car["price"])<min_price:
        min_price=int(car["price"])


def is_min(min_price):
    for car in cars:
        if int(car["price"])==min_price:
            return car["model"]


print("The cheapest car is", is_min(min_price))


