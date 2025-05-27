from app.habit import create_user, create_habit

def main_menu():
    while True:
        print("\n=== Positive Habit Generator ===")
        print("1. Create a user")
        print("2. Add a habit")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            create_user(name)
            print("User created!")
        elif choice == "2":
            user_id = int(input("Enter your user ID: "))
            habit_name = input("Enter habit name: ")
            frequency = input("Enter frequency (daily, weekly, etc): ")
            category = input("Enter category: ")
            create_habit(user_id, habit_name, frequency, category)
            print("Habit added!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def main_cli():
    main_menu()

