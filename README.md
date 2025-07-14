def calculate_area_of_circle(radius):
    """
    Calculates the area of a circle.
    This function contains a deliberate error for CodeRabbit AI to detect.
    """
    pi = 3.14159
    # Intentional error: Incorrect formula for area (should be pi * radius**2)
    area = pi * radius * 2  # This is incorrect, it calculates circumference if radius is 1
    return area

def main():
    r = 5
    area = calculate_area_of_circle(r)
    print(f"The area of a circle with radius {r} is: {area}")

if __name__ == "__main__":
    main()
