from save import save_total_car

def delete_car(total_cars):
    search = input("Enter the car name which you want to remove: ")
    delete_car = []
    for index, car in enumerate(total_cars):
        if search in car['name']:
            delete_car.append((index, car))
    index_number = int(input("Enter your index number: "))
    car_index = [index_number- 1][0]
    delete_car_index = total_cars[car_index]
    total_cars.pop(car_index)
    save_total_car(total_cars)
    return total_cars 
