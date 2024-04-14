list_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0

for i in range(len(list_cars)):
    cars_count += 10
    print('Я езжу на автомобиле марки', list_cars[i])

print(cars_count)

print()

for i in range(len(list_cars)):
    list_cars[2] = "AUDI"
    print('Я езжу на автомобиле марки', list_cars[i])

