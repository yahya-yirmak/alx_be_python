
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if choice == 1:
            name = input('Enter the item to add: ')
            if name in shopping_list:
                print(f'{name} already exists.')
            else:
                shopping_list.append(name)

        elif choice == 2:
            name = input('Enter the item to remove: ')
            if name in shopping_list:
                shopping_list.remove(name)
            else:
                print(f'{name} does not exist.')
        
        elif choice == 3:
            print(f"Shopping list: {shopping_list}")

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()