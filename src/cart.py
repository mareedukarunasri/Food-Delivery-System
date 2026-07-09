cart_items = []


def add_to_cart(item, price, quantity):
    cart_items.append({
        "item": item,
        "price": price,
        "quantity": quantity
    })


def view_cart():
    total = 0

    print("\nYour Cart:")

    for item in cart_items:
        amount = item["price"] * item["quantity"]
        total += amount
        print(item["item"], "-", amount)

    print("Total:", total)