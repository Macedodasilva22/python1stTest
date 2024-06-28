from cars.menu import main_menu
from problems.problems import choose_problem


main_menu = []


def Add_car():
    new_car = input("Which car do you want to add? ")

    issue = input("Is there a problem with the car? (yes/no): ").lower()

    if issue == 'yes':
        issue_description = choose_problem()

        if issue_description:
            main_menu.append((new_car, issue_description))
        else:
            main_menu.append(new_car)

    else:
        main_menu.append(new_car)

    print("Car added successfully.")


def delete_car():
    car_to_delete = input("Which car do you want to delete? ")
    global main_menu
    
    for car in main_menu[:]:
        if car[0].lower() == car_to_delete.lower():
            main_menu.remove(car)
            print(f"{car_to_delete} has been deleted from the list.")
            return
    
    print(f"Error: {car_to_delete} is not found in the list.")



def search_car(car_list):
    car_list = main_menu
    search_term = input("Enter the car you want to search for: ")
    if search_term in car_list:
        print(f"{search_term} is found in the list of cars.")
    else:
        print(f"{search_term} is not found in the list of cars.")
