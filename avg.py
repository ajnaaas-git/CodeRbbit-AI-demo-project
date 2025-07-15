

def calculate_average(num1, num2, num3):
    sum_of_numbers = num1 + num2 + num3
    average = sum_of_numbers / 3
    return avg


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))


result = calculate_average(number1, number2, number3)
print(f"The average is: {result}")
