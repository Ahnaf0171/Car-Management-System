"""car showrooom management system
    car name , car model, car model year,milage,  condition , car price   """
from save import save_total_car
def add_car(total_cars):
    name = input("Enter your car name: ")
    model = input("Enter your car model: ")
    model_year = int(input("Enter your model Year: "))
    milage = float(input("Enter your car milage: "))
    condition = input("Enter your car condition: ")
    price = int(input("Enter your car price: "))

    car = {
        "name" : name,
        "model" : model,
        "model_year": model_year,
        "milage": milage,
        "condition": condition,
        "price": price
        }
    total_cars.append(car)
    save_total_car(total_cars)
    print("car Added Successfully")
    return total_cars
