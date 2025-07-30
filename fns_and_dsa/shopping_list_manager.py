def display_menu():
    print("\nShopping List Manager")
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
            item = input("Enter the item to add: ").strip()
            if item:  # make sure user doesn't enter an empty string
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to the shopping list.")
            else:
                print("⚠️ You must enter a valid item name.")
                
        elif choice == '2':
            if not shopping_list:
                print("⚠️ The shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"🗑️ '{item}' has been removed from the shopping list.")
                else:
                    print(f"❌ '{item}' was not found in the shopping list.")
                    
        elif choice == '3':
            if shopping_list:
                print("\n🛒 Current Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("🛒 Your shopping list is empty.")
                
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
