"""car showrooom management system
    car name , car model, car model year,milage,  condition , car price   """
import add
import delete
import update
import view 
total_cars = []
text = "Welcome to  Ahnaf Car Showroom"
print(text)
while True:
    option = """1. Add Car
    2. View Car
    3. Update
    4. Delete
    5. Exit"""
    print(option)
    num = input ("Choose an Option: ")
    
    if num == "1":
        total_cars = add.add_car(total_cars)
    elif num == "2":
        total_cars = view.view_car(total_cars)
    elif num == "3":
        total_cars = update.update_car(total_cars)
    elif num == "4":
        total_cars = delete.delete_car(total_cars)
    elif num == "5":
        break
    else:
        print("Invalid Input")
        

