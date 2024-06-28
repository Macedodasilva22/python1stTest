def choose_problem():
    print("Choose an a problem:")
    print("1. Engine problem")
    print("2. Transmission problem")
    print("3. Electrical problem")
    print("4. Other issue")
    
    option = input("Enter the number corresponding to the issue: ")
    
    if option == '1':
        return "Engine problem -2000 NIS"
    elif option == '2':
        return "Breaks problem - 1000 NIS"
    elif option == '3':
        return "5000 km treatment - 500 NIS"
    elif option == '4':
        return "10,000 km treatment - 1000 NIS"
    elif option == '5':
        return "Filters + Oil - 250 NIS"
    elif option == '6':
        return "Gear - 1000 NIS"
    
    elif option == '7':
        return input("Enter other issue: ")
    else:
        print("Invalid option. No issue will be recorded.")
        return None
