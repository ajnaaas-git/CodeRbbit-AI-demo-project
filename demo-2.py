
def calculate_sum(a, b) 
    result = a + b
    print(f"The sum is: {result}")


def greet_user():
    print(f"Hello, {user_name}!")


def divide_numbers(numerator, denominator):
    try:
        quotient = numerator / denominator
        print(f"The quotient is: {quotient}")
    except TypeError:
        print("Error: Cannot divide incompatible types.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


def access_list_element():
    my_list = [10, 20, 30]
    print(f"Element at index 3: {my_list[3]}")


def manipulate_string():
    text = "Python"
    print(text.to_upper_case()) 

if __name__ == "__main__":
    print("--- Demonstrating SyntaxError ---")
   
    print("\n--- Demonstrating NameError ---")
   
    print("\n--- Demonstrating TypeError and ZeroDivisionError ---")
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers("abc", 5) 

    print("\n--- Demonstrating IndexError ---")
  
    print("\n--- Demonstrating AttributeError ---")
   
