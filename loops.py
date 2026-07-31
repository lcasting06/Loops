def menu():
    print()
    print("Taco Palace Menu")
    print("1. Taco - $2.75")
    print("2. Burrito - $5.50")
    print("3. Nachos - $4.87")
    print("4. Soft Drink - $1.99")
    print("5. Quit")

def price(choice):
    if choice == 1:
        return 2.75
    elif choice == 2:
        return 5.50
    elif choice == 3:
        return 4.87
    elif choice == 4:
        return 1.99

print("Welcome to Taco Palace!")
print("Please view the menu below and enter the number that represents your selection.")

orders = []
total = 0

while True:
    menu()

    choice = int(input("Enter your selection: "))

    if choice == 1:
        print("You selected a Taco.")
        orders.append("Taco")
        total = total + price(choice)

    elif choice == 2:
        print("You selected a Burrito.")
        orders.append("Burrito")
        total = total + price(choice)

    elif choice == 3:
        print("You selected Nachos.")
        orders.append("Nachos")
        total = total + price(choice)

    elif choice == 4:
        print("You selected a Soft Drink.")
        orders.append("Soft Drink")
        total = total + price(choice)

    elif choice == 5:
        break

    else:
        print("Please select 1-5.")

print()
print("Your order:")

for item in orders:
    print(item)

print("Your total is $%.2f" % total)
