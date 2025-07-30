from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    print("📅 Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"📆 The date after {days_to_add} days will be:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()

    # Ask user for number of days to add
    try:
        days = int(input("\nEnter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("❌ Please enter a valid integer for days.")

if __name__ == "__main__":
    main()
