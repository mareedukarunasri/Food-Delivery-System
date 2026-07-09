restaurants = [
    {"id": 1, "name": "Paradise Biryani"},
    {"id": 2, "name": "Dominos Pizza"},
    {"id": 3, "name": "Burger King"}
]


def view_restaurants():
    print("\nAvailable Restaurants:")
    for r in restaurants:
        print(r["id"], "-", r["name"])