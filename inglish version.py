import random

def MenuClients():
    print("\nWelcome to the Radiant Cow Steak House!")
    print("----------------------------------------")
    print("|            MAIN MENU                 |")
    print("----------------------------------------")
    print("|  APPETIZERS                          |")
    print("| 1. Beef Carpaccio         €15.00     |")
    print("| 2. Beef Tartare           €16.00     |")
    print("| 3. Mixed Bruschetta       €8.00      |")
    print("----------------------------------------")
    print("|  MAIN COURSES                        |")
    print("| 4. Tagliatelle with Ragù  €14.00     |")
    print("| 5. Mushroom Risotto       €13.00     |")
    print("| 6. Gnocchi with Gorgonzola €12.00    |")
    print("----------------------------------------")
    print("|  MEAT DISHES                         |")
    print("| 7. Ribeye Steak (300g)    €28.00     |")
    print("| 8. Filet (250g)           €32.00     |")
    print("| 9. T-Bone (500g)          €35.00     |")
    print("| 10. Tomahawk (800g)       €45.00     |")
    print("----------------------------------------")
    print("|  SIDES                              |")
    print("| 11. Roasted Potatoes      €5.00      |")
    print("| 12. Grilled Vegetables    €6.00      |")
    print("| 13. Mixed Salad           €4.00      |")
    print("----------------------------------------")
    print("|  DRINKS                             |")
    print("| 14. House Wine            €18.00     |")
    print("| 15. Craft Beer            €6.00      |")
    print("| 16. Mineral Water         €2.50      |")
    print("----------------------------------------")
    print("|  DESSERTS                          |")
    print("| 17. Tiramisu              €6.00      |")
    print("| 18. Panna Cotta           €5.00      |")
    print("| 19. Cheesecake            €6.00      |")
    print("----------------------------------------")
    print("|  AFTER MEAL                         |")
    print("| -1- Coffee              €1.00       |")
    print("| -2- Digestive           €4.00       |")
    print("----------------------------------------")
    print ("")
    total = 0
    while True:
        try:
            choice = input("\nEnter the number of the dish you'd like to order (0 to finish): ")
            choice = int(choice)

            if 1 <= choice <= 19:
                print(f"You selected dish number {choice}")
            else:
                print("Please select a valid number from the menu (1-19)")

            if choice == 1:
                total += 15
            if choice == 2:
                total += 16
            if choice == 3:
                total += 8
            if choice == 4:
                total += 14
            if choice == 5:
                total += 13
            if choice == 6:
                total += 12
            if choice == 7:
                total += 28
            if choice == 8:
                total += 32
            if choice == 9:
                total += 35
            if choice == 10:
                total += 45
            if choice == 11:
                total += 5
            if choice == 12:
                total += 6
            if choice == 13:
                total += 4
            if choice == 14:
                total += 18
            if choice == 15:
                total += 6
            if choice == 16:
                total += 2.50
            if choice == 17:
                total += 6
            if choice == 18:
                total += 5
            if choice == 19:
                total += 6
            if choice == 0:
                print("Thank you for ordering!")
                for i in range(5):
                    print("")

                luck = random.randint(0, 1)
                print(f"I hope everything was to your liking. The total is €{total}")
                print("")
                print("Would you like a coffee (-1-) or a digestive (-2-)? (any other number for no)")
                beverage = input()
                if beverage == "1":
                    print("Here's your coffee")
                    if luck == 0:
                        total += 1
                        print("")
                        print(f"Including the coffee, the total is €{total}")
                    else:
                        print("The coffee is on the house")
                        print("")
                        print(f"So it's €{total}")
                elif beverage == "2":
                    print("Here's your digestive")
                    if luck == 0:
                        total += 4
                        print()
                        print(f"Including the digestive, the total is €{total}")
                    else:
                        print("The digestive is on the house")
                        print("")

                break
        except ValueError:
            print("Please enter a valid number.")

def tables():
    return random.randint(1, 21)


def selectRole():
    print("Welcome to the program. Enter mode 1 - 'Client' or 2 - 'Employee'")
    while True:
        choice = input()
        if choice == '1':
            table_number = tables()
            print("Welcome, client, to the Radiant Cow Steak House")
            print("")
            print(f"Please take a seat at table {table_number}")
            print("Here is the menu! Take your time to choose.")
            MenuClients()
            return choice
        
        if choice == "2":
            while True:
                print("Hi! Have I seen you somewhere before? (1 - Yes, 2 - No)")
                seen_before = input()
                if seen_before == "1":
                    print("Enter your code so I can confirm I know you.")
                    while True:
                        entered_code = input()
                        if entered_code == str(code):
                            print(f"Oh yes, now I remember you. You're {name} and you're {age} years old.")
                            work_hours = random.randint(1, 9) 
                            start_hour = random.randint(0, 23)
                            start_minute = random.randint(0, 59)
                            start_time = start_hour, start_minute
                            end_hour = start_hour + work_hours
                            end_time = end_hour, start_minute
                            print(f"Your shift is {work_hours} hours, from {start_time} to {end_time}.")
                            break
                        else:
                            print("Invalid code, try again.")

                elif seen_before == "2":
                    print("Ah, I see! I thought I hadn't seen you around before. Are you new? What's your name?")
                    name = input()
                    print(f"{name}, eh? That's a great name! How old are you?")
                    age = input()
                    print(f"So you're {age} years old, huh? You look great for your age.")
                    print("")
                    print("Alright, I'll give you your code now. Please don't lose it.")
                    print("")
                    code = random.randint(1000000, 99999999)
                    print(f"Here's your code: {code}")

            else:
                print("Invalid choice. Please enter 1 or 2.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    selectRole()

if __name__ == "__main__":
    main()
