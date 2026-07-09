from src.user import register
from src.login import login

while True:
    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. User Registration")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank you for using the Food Delivery System!")
        break
    else:
        print("Invalid Choice")