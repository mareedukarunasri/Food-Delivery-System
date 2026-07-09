from src.user import register
from src.login import login
from src.restaurant import view_restaurants
from src.menu import view_menu
from src.cart import add_to_cart, view_cart
from src.payment import payment
from src.admin import admin_panel
from src.database import connect_database


# Database connection
connect_database()


while True:

    print("\n===== Food Delivery System =====")
    print("1. User Registration")
    print("2. Login")
    print("3. View Restaurants")
    print("4. View Menu")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Payment")
    print("8. Admin Panel")
    print("9. Exit")


    choice = int(input("Enter your choice: "))


    if choice == 1:
        register()

    elif choice == 2:
        login()

    elif choice == 3:
        view_restaurants()

    elif choice == 4:
        restaurant_id = int(input("Enter Restaurant ID: "))
        view_menu(restaurant_id)

    elif choice == 5:
        item = input("Enter food item: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        add_to_cart(item, price, quantity)


    elif choice == 6:
        view_cart()


    elif choice == 7:
        payment()


    elif choice == 8:
        admin_panel()


    elif choice == 9:
        print("Thank you for using Food Delivery System!")
        break


    else:
        print("Invalid choice")