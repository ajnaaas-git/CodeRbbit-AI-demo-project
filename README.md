# This program contains various types of errors for demonstration purposes.

# 1. SyntaxError: Missing colon in function definition
def calculate_sum(a, b) 
    result = a + b
    print(f"The sum is: {result}")

# 2. NameError: Using an undefined variable
def greet_user():
    print(f"Hello, {user_name}!")

# 3. TypeError: Performing an invalid operation between incompatible types
def divide_numbers(numerator, denominator):
    try:
        quotient = numerator / denominator
        print(f"The quotient is: {quotient}")
    except TypeError:
        print("Error: Cannot divide incompatible types.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 4. IndexError: Accessing an out-of-bounds index in a list
def access_list_element():
    my_list = [10, 20, 30]
    print(f"Element at index 3: {my_list[3]}")

# 5. AttributeError: Trying to call a non-existent method on an object
def manipulate_string():
    text = "Python"
    print(text.to_upper_case()) # Incorrect method name

# Main execution block
if __name__ == "__main__":
    print("--- Demonstrating SyntaxError ---")
    # This line will cause a SyntaxError when the program is run
    # calculate_sum(5, 7) # Uncomment to see the SyntaxError

    print("\n--- Demonstrating NameError ---")
    # This line will cause a NameError
    # greet_user() # Uncomment to see the NameError

    print("\n--- Demonstrating TypeError and ZeroDivisionError ---")
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers("abc", 5) # This will trigger the TypeError handler

    print("\n--- Demonstrating IndexError ---")
    # This line will cause an IndexError
    # access_list_element() # Uncomment to see the IndexError

    print("\n--- Demonstrating AttributeError ---")
    # This line will cause an AttributeError
    # manipulate_string() # Uncomment to see the AttributeError
