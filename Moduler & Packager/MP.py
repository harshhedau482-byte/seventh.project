"""
main.py - Multi-Utility Toolkit Main Entry Point

A menu-driven console application that integrates multiple standard modules,
custom modules, and packages to perform a variety of tasks.

Modules Used:
    - datetime: Date and time operations
    - time: Stopwatch and countdown timer
    - math: Mathematical computations
    - random: Random data generation
    - uuid: Unique identifier generation
    - toolkit_package.file_operations: Custom file handling
    - toolkit_package.math_utilities: Custom math utilities

Author: [Your Name]
Date: [Current Date]
"""

import sys
import time
import math
import random
import uuid
import string
from datetime import datetime, timedelta

from toolkit_package import file_operations
from toolkit_package import math_utilities


# ============================================================
# Datetime and Time Operations
# ============================================================

def display_current_datetime():
    """Display current date and time in a user-friendly format."""
    now = datetime.now()
    print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Formatted: {now.strftime('%A, %B %d, %Y at %I:%M %p')}")


def calculate_date_difference():
    """Calculate the difference between two dates."""
    try:
        date1_str = input("Enter the first date (YYYY-MM-DD): ").strip()
        date2_str = input("Enter the second date (YYYY-MM-DD): ").strip()
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        difference = abs((date2 - date1).days)
        print(f"Difference: {difference} days")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")


def format_custom_date():
    """Format a date into a custom format."""
    try:
        date_str = input("Enter a date (YYYY-MM-DD): ").strip()
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        print("\nCustom Formats:")
        print(f"  ISO Format:        {date_obj.strftime('%Y-%m-%d')}")
        print(f"  Long Format:       {date_obj.strftime('%B %d, %Y')}")
        print(f"  Short Format:      {date_obj.strftime('%d/%m/%Y')}")
        print(f"  Day of Week:       {date_obj.strftime('%A')}")
        print(f"  Time-less:         {date_obj.strftime('%d-%b-%Y')}")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")


def stopwatch():
    """A simple stopwatch using the time module."""
    print("\nStopwatch started. Press Enter to stop...")
    start_time = time.time()
    input()
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")


def countdown_timer():
    """A simple countdown timer."""
    try:
        seconds = int(input("Enter countdown time in seconds: ").strip())
        if seconds <= 0:
            print("Error: Please enter a positive number.")
            return
        print(f"\nCountdown started for {seconds} seconds...")
        for i in range(seconds, 0, -1):
            print(f"  {i} seconds remaining...", end="\r")
            time.sleep(1)
        print("\nTime's up!")
    except ValueError:
        print("Error: Please enter a valid integer.")


def datetime_menu():
    """Sub-menu for datetime and time operations."""
    while True:
        print("\n--- Datetime and Time Operations ---")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_current_datetime()
        elif choice == '2':
            calculate_date_difference()
        elif choice == '3':
            format_custom_date()
        elif choice == '4':
            stopwatch()
        elif choice == '5':
            countdown_timer()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")


# ============================================================
# Mathematical Operations
# ============================================================

def calculate_factorial():
    """Calculate factorial of a number."""
    try:
        num = int(input("Enter a number: ").strip())
        result = math_utilities.factorial(num)
        print(f"Factorial: {result}")
    except ValueError as e:
        print(f"Error: {e}")


def solve_compound_interest():
    """Solve compound interest."""
    try:
        principal = float(input("Enter principal amount: ").strip())
        rate = float(input("Enter rate of interest (in %): ").strip())
        time_years = float(input("Enter time (in years): ").strip())
        amount, interest = math_utilities.compound_interest(principal, rate, time_years)
        print(f"Compound Interest: {amount:.2f}")
        print(f"Interest Earned: {interest:.2f}")
    except ValueError:
        print("Error: Please enter valid numeric values.")


def trigonometric_calculations():
    """Perform trigonometric calculations."""
    try:
        angle = float(input("Enter angle in degrees: ").strip())
        radians = math.radians(angle)
        print(f"\nTrigonometric values for {angle}°:")
        print(f"  sin: {math.sin(radians):.4f}")
        print(f"  cos: {math.cos(radians):.4f}")
        print(f"  tan: {math.tan(radians):.4f}")
    except ValueError:
        print("Error: Please enter a valid number.")


def area_of_shapes():
    """Calculate area of geometric shapes."""
    print("\n--- Area of Geometric Shapes ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == '1':
            radius = float(input("Enter radius: ").strip())
            print(f"Area of Circle: {math_utilities.area_circle(radius)}")
        elif choice == '2':
            length = float(input("Enter length: ").strip())
            width = float(input("Enter width: ").strip())
            print(f"Area of Rectangle: {math_utilities.area_rectangle(length, width)}")
        elif choice == '3':
            base = float(input("Enter base: ").strip())
            height = float(input("Enter height: ").strip())
            print(f"Area of Triangle: {math_utilities.area_triangle(base, height)}")
        elif choice == '4':
            side = float(input("Enter side: ").strip())
            print(f"Area of Square: {math_utilities.area_square(side)}")
        else:
            print("Invalid shape choice.")
    except ValueError:
        print("Error: Please enter valid numeric values.")


def math_menu():
    """Sub-menu for mathematical operations."""
    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Unit Conversions")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            calculate_factorial()
        elif choice == '2':
            solve_compound_interest()
        elif choice == '3':
            trigonometric_calculations()
        elif choice == '4':
            area_of_shapes()
        elif choice == '5':
            unit_conversions()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")


def unit_conversions():
    """Perform unit conversions."""
    print("\n--- Unit Conversions ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    choice = input("Enter your choice: ").strip()

    try:
        if choice == '1':
            c = float(input("Enter temperature in Celsius: ").strip())
            print(f"{c}°C = {math_utilities.celsius_to_fahrenheit(c):.2f}°F")
        elif choice == '2':
            f = float(input("Enter temperature in Fahrenheit: ").strip())
            print(f"{f}°F = {math_utilities.fahrenheit_to_celsius(f):.2f}°C")
        elif choice == '3':
            km = float(input("Enter distance in kilometers: ").strip())
            print(f"{km} km = {math_utilities.km_to_miles(km):.2f} miles")
        elif choice == '4':
            miles = float(input("Enter distance in miles: ").strip())
            print(f"{miles} miles = {math_utilities.miles_to_km(miles):.2f} km")
        elif choice == '5':
            kg = float(input("Enter weight in kilograms: ").strip())
            print(f"{kg} kg = {math_utilities.kg_to_pounds(kg):.2f} pounds")
        elif choice == '6':
            pounds = float(input("Enter weight in pounds: ").strip())
            print(f"{pounds} pounds = {math_utilities.pounds_to_kg(pounds):.2f} kg")
        else:
            print("Invalid conversion choice.")
    except ValueError:
        print("Error: Please enter valid numeric values.")


# ============================================================
# Random Data Generation
# ============================================================

def generate_random_number():
    """Generate a random number within a range."""
    try:
        low = int(input("Enter lower bound: ").strip())
        high = int(input("Enter upper bound: ").strip())
        if low > high:
            print("Error: Lower bound must be less than or equal to upper bound.")
            return
        print(f"Random Number: {random.randint(low, high)}")
    except ValueError:
        print("Error: Please enter valid integers.")


def generate_random_list():
    """Generate a random list of numbers."""
    try:
        size = int(input("Enter list size: ").strip())
        low = int(input("Enter lower bound: ").strip())
        high = int(input("Enter upper bound: ").strip())
        random_list = [random.randint(low, high) for _ in range(size)]
        print(f"Random List: {random_list}")
    except ValueError:
        print("Error: Please enter valid integers.")


def create_random_password():
    """Create a random password."""
    try:
        length = int(input("Enter password length: ").strip())
        if length < 4:
            print("Error: Password length should be at least 4.")
            return
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid integer.")


def generate_otp():
    """Generate a random OTP."""
    otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
    print(f"Generated OTP: {otp}")


def random_sampling():
    """Simulate random sampling from a dataset."""
    dataset = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    print(f"\nDataset: {dataset}")
    try:
        sample_size = int(input("Enter sample size: ").strip())
        if sample_size > len(dataset):
            print("Error: Sample size exceeds dataset size.")
            return
        sample = random.sample(dataset, sample_size)
        print(f"Random Sample: {sample}")
    except ValueError:
        print("Error: Please enter a valid integer.")


def random_menu():
    """Sub-menu for random data generation."""
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling from Dataset")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            generate_random_number()
        elif choice == '2':
            generate_random_list()
        elif choice == '3':
            create_random_password()
        elif choice == '4':
            generate_otp()
        elif choice == '5':
            random_sampling()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")


# ============================================================
# UUID Generation
# ============================================================

def generate_uuid():
    """Generate a unique identifier using uuid4()."""
    unique_id = uuid.uuid4()
    print(f"\nGenerated UUID: {unique_id}")
    print(f"UUID Version: {unique_id.version}")
    print(f"UUID String:  {str(unique_id)}")


def generate_multiple_uuids():
    """Generate multiple UUIDs for different purposes."""
    print("\nGenerating UUIDs for different purposes:")
    print(f"  File ID:    {uuid.uuid4()}")
    print(f"  Record ID:  {uuid.uuid4()}")
    print(f"  Session ID: {uuid.uuid4()}")


def uuid_menu():
    """Sub-menu for UUID operations."""
    while True:
        print("\n--- Generate Unique Identifiers (UUID) ---")
        print("1. Generate a single UUID")
        print("2. Generate multiple UUIDs")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            generate_uuid()
        elif choice == '2':
            generate_multiple_uuids()
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


# ============================================================
# File Operations (Custom Module)
# ============================================================

def file_operations_menu():
    """Sub-menu for file operations using the custom module."""
    while True:
        print("\n--- File Operations ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Delete a file")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            filename = input("Enter file name: ").strip()
            print(file_operations.create_file(filename))
        elif choice == '2':
            filename = input("Enter file name: ").strip()
            data = input("Enter data to write: ").strip()
            print(file_operations.write_to_file(filename, data))
        elif choice == '3':
            filename = input("Enter file name: ").strip()
            print("\nFile Content:")
            print(file_operations.read_from_file(filename))
        elif choice == '4':
            filename = input("Enter file name: ").strip()
            data = input("Enter data to append: ").strip()
            print(file_operations.append_to_file(filename, data))
        elif choice == '5':
            filename = input("Enter file name: ").strip()
            confirm = input(f"Delete '{filename}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print(file_operations.delete_file(filename))
            else:
                print("Deletion cancelled.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")


# ============================================================
# Dynamic Module Exploration (dir())
# ============================================================

def explore_module_attributes():
    """Explore attributes of a module using dir()."""
    print("\n--- Explore Module Attributes (dir()) ---")
    print("Available modules to explore:")
    print("  Built-in: math, random, datetime, time, uuid, string, sys, os")
    print("  Custom:   toolkit_package.file_operations, toolkit_package.math_utilities")
    module_name = input("Enter module name to explore: ").strip()

    try:
        # Dynamically import the module
        if module_name.startswith("toolkit_package"):
            parts = module_name.split(".")
            module = __import__(module_name, fromlist=[''])
        else:
            module = __import__(module_name)

        attributes = dir(module)
        print(f"\nAvailable Attributes in {module_name} module:")
        print(attributes)
        print(f"\nTotal attributes: {len(attributes)}")

    except ImportError:
        print(f"Error: Module '{module_name}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# ============================================================
# Main Menu
# ============================================================

def display_main_menu():
    """Display the main menu."""
    print("\n" + "=" * 55)
    print("       Welcome to Multi-Utility Toolkit")
    print("=" * 55)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 55)


def main():
    """Main program loop."""
    print("=" * 60)
    print("Welcome to the Multi-Utility Toolkit!")
    print("=" * 60)
    print("This toolkit demonstrates Python's modular structure using")
    print("built-in modules, custom modules, and packages.\n")

    while True:
        display_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            uuid_menu()
        elif choice == '5':
            file_operations_menu()
        elif choice == '6':
            explore_module_attributes()
        elif choice == '7':
            print("\nThank you for using the Multi-Utility Toolkit! Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")

        input("\nPress Enter to continue...")


# The __name__ == "__main__" paradigm ensures main() runs only
# when this script is executed directly, not when imported.
if __name__ == "__main__":
    main()
