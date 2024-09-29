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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").lower()
            if item not in shopping_list:
                shopping_list.append(item)
                # shopping_list +=1
                print(f"Your item has been added {shopping_list}")
            # pass
        elif choice == '2':
            # Prompt for and remove an item
            user_input = input("Remove your shopping list: ").lower()
            try:
                shopping_list.remove(user_input)
                print(f"Your item {user_input} has been removed {shopping_list}")
            
            except ValueError:
                print(f"Your item is not in Shopping List: {shopping_list}")

            # pass
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Shopping list is empty")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f'{index}. {item}')
            # pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()