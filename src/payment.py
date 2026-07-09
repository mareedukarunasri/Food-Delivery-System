def make_payment():

    print("\nPayment Options")
    print("1. UPI")
    print("2. Cash on Delivery")

    choice = input("Choose payment: ")

    if choice == "1":
        print("Payment successful using UPI")

    elif choice == "2":
        print("Order placed with Cash on Delivery")

    else:
        print("Invalid payment option")