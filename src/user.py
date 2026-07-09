users = []

def register():
    print("\n===== User Registration =====")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    user = {
        "name": name,
        "email": email,
        "password": password
    }

    users.append(user)

    print("\nRegistration Successful!")