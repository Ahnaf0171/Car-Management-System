"""car showrooom management system
    car name , car model, car model year,milage,  condition , car price   """
def view_car(total_cars):
    if total_cars != []:
        for car in total_cars:
            print(f"Car Name: {car['name']}\n car Model: {car['model']}\n Car model Year: {car['model_year']}\n Car Milage: {car['milage']}\n Car Condition: {car['condition']}\n Car price: {car['price']}")
    else:
        print(f"No Car found")
    return total_cars