from app.habit import create_user, create_habit
from app.models import User
from app.database import Session

def display_users():
    """Helper function to display all users"""
    session = Session()
    users = session.query(User).all()
    if not users:
        print("No users found. Please create a user first.")
        return False
    print("\nAvailable Users:")
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}")
    return True

def main_menu():
    while True:
        print("\n=== Positive Habit Generator ===")
        print("1. Create a user")
        print("2. Add a habit")
        print("3. List all users")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter your name: ").strip()
            if name:  # Check if name is not empty
                create_user(name)
                print(f"User '{name}' created!")
            else:
                print("Name cannot be empty!")
                
        elif choice == "2":
            if display_users():  # Only proceed if users exist
                while True:
                    try:
                        user_id = int(input("\nEnter your user ID: "))
                        habit_name = input("Enter habit name: ").strip()
                        if not habit_name:
                            print("Habit name cannot be empty!")
                            continue
                            
                        frequency = input("Enter frequency (daily, weekly, etc): ").strip()
                        category = input("Enter category: ").strip()
                        
                        create_habit(user_id, habit_name, frequency, category)
                        print(f"Habit '{habit_name}' added!")
                        break
                    except ValueError:
                        print("Please enter a valid number for user ID!")
                    except Exception as e:
                        print(f"Error: {e}")
                        break
                        
        elif choice == "3":
            display_users()
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

def main_cli():
    main_menu()

