menus = {
    1: [
        {"item": "Chicken Biryani", "price": 250},
        {"item": "Veg Biryani", "price": 150}
    ],

    2: [
        {"item": "Pizza", "price": 300},
        {"item": "Burger", "price": 120}
    ],

    3: [
        {"item": "Veg Burger", "price": 100},
        {"item": "French Fries", "price": 80}
    ]
}


def view_menu(restaurant_id):
    print("\nFood Menu:")

    for item in menus[restaurant_id]:
        print(item["item"], "-", item["price"])