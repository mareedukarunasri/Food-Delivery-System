from src.user import register

while True:
    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. User Registration")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")