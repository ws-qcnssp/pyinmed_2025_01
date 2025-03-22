def display_user_info(user):
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"City: {user['city']}")

user_data = {'name': 'Alice', 'age': 30}
display_user_info(user_data)

extra_user_data = {'name': 'Bob', 'age': 40, 'city': 'New York'}
display_user_info(extra_user_data)
