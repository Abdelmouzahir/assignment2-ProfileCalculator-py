print("Welcome to Circle Phones' Profit calculator.")

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday','Sunday']

while True:   
    print("You can calculate the profit of the company according to a specific day or by a week or divide \n the week into weekdays and weekend.")

    print(" Enter: ")
    print(" 1 - For specific Day")
    print(" 2 - For the Week")
    print(" 3 - For Week Business Days")
    print(" 4 - For Weekend days")
    print(" 0 - Exit")

    
    period = int(input(" "))
    if  period == 0:
        print("Program End!")
        break        

    if period ==1:
        days = [input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]:\n ").capitalize()]
        printed_period = days[0]
    elif period == 2:
        days = weekdays
        printed_period = "week"
    elif period == 3:
        days = weekdays[:5]
        printed_period = "week (buisness days)"  
    elif period == 4:
        days = weekdays[-2:]
        printed_period = "weekend"      
    else:
        print("Invalid input. Please enter a number between 1 and 4 or 0 to stop the program!")
        continue
        
    total_profit = 0
    profit_dictionary = {
        1 : 120.45,
        2 : 99.50,
        3 : 75.69,
        4 : 65.73,
        5 : 51.49
    }
    for day in days:
        print(f"For {day}")
        while True:
            category = input("Enter the product category (1-5) or 0 to stop: \n ")
            try:
                val_category = int(category)
                if val_category >= 1 and val_category <= 5:
                    quantity = input("Enter quantity sold: \n ")
                    try:
                        val_quantity = int(quantity)
                        profit_calculation = val_quantity * profit_dictionary[val_category]
                        total_profit += profit_calculation 
                    except ValueError:
                        False   
                elif val_category == 0:
                    break
                else:
                    print("Invalid input, please enter a valid number")
            except ValueError:
                print("Please enter an input number!")

    if period == 1:
        print(f"\nYour total profit for {days[0]}: ${total_profit:.2f}")
    elif period == 2:
        print(f"\nYour total profit for the week: ${total_profit:.2f}")
    elif period == 3:
        print(f"\nYour total profit for the week (business days): ${total_profit:.2f}")
    elif period == 4:
        print(f"\nYour total profit for the weekend: ${total_profit:.2f}")            


    if total_profit >= 10000:
        print(f"You did well this {printed_period}! Keep up the great work!")
    else:
        print(f"We didn't reach our goal for this {printed_period}. More work is needed.") 

                  