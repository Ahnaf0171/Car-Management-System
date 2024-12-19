"""car showrooom management system
    car name , car model, car model year,milage,  condition , car price   """

def save_total_car(total_cars):
    with open("car.csv", "w") as file:
        for car in total_cars:
            index = f"{car['name']}, {car['model'], car['model_year'], car['milage'], car['condition'], car['price']}\n"
            file.write(index)
        