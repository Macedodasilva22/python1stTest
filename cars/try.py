def main_menu():
    while True:
        print("1 - Add a Car")
        print("2 - Delete a Car")
        print("3 - Search a Car")
        print("4 - Exit")
        choise = input("Enter your selection: ")
        
        if choise == "1":
            print("Adding a car")
       
        elif choise == "2":
            print("Deleting a car")
           
        elif choise == "3":
            print("Searching for a car")
           
        elif choise == "4":
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

