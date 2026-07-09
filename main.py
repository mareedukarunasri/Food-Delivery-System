from src.user import register
from src.login import login
from src.restaurant import view_restaurants
from src.menu import view_menu

while True:
    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. User Registration")
    print("2. Login")
    print("3. View Restaurants")
    print("4. View Menu")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        view_restaurants()
    elif choice == "4":
        restaurant_id = int(input("Enter restaurant ID: "))
        view_menu(restaurant_id)
    elif choice == "5":
        print("Thank you for using the Food Delivery System!")
        break
    else:
        print("Invalid Choice")