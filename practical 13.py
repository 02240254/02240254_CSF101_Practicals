import unittest
import math

# Exercise 1: Handle Division by Zero
def safe_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    return result

# Exercise 2: Validate Age Range
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120.")
    return f"Age {age} is valid."

# Exercise 3: Square Root Calculation
def calculate_square_root(x):
    try:
        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(x)
    except ValueError as ve:
        return str(ve)

# Exercise 4: Unit Test for String Reversal
def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

# Exercise 5: Custom Exception for Temperature
class InvalidTemperatureError(Exception):
    pass

def set_temperature(temp):
    if temp < -273.15:
        raise InvalidTemperatureError(f"Temperature {temp}°C is below absolute zero!")
    return f"Temperature set to {temp}°C."

# Exercise 6: Implement Try-Except for File Handling
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)

# Exercise 7: Check if Number is Even or Odd
def check_even_odd(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return "Even" if number % 2 == 0 else "Odd"

# Unit tests for the exercises
class TestExercises(unittest.TestCase):
    # Test Exercise 1: Division by Zero
    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5.0)
        self.assertEqual(safe_divide(10, 0), "Cannot divide by zero")
    
    # Test Exercise 2: Age Validation
    def test_validate_age(self):
        self.assertEqual(validate_age(25), "Age 25 is valid.")
        with self.assertRaises(InvalidAgeError):
            validate_age(150)
    
    # Test Exercise 3: Square Root Calculation
    def test_calculate_square_root(self):
        self.assertEqual(calculate_square_root(9), 3.0)
        self.assertEqual(calculate_square_root(-9), "Cannot calculate the square root of a negative number.")
    
    # Test Exercise 4: String Reversal
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("!@#$"), "$#@!")
        with self.assertRaises(ValueError):
            reverse_string(123)
    
    # Test Exercise 5: Temperature Check
    def test_set_temperature(self):
        self.assertEqual(set_temperature(25), "Temperature set to 25°C.")
        with self.assertRaises(InvalidTemperatureError):
            set_temperature(-300)
    
    # Test Exercise 6: File Handling
    def test_read_file(self):
        # You can change the path to an actual file for testing
        self.assertEqual(read_file("existing_file.txt"), "File not found")  # Assuming file doesn't exist

    # Test Exercise 7: Check Even or Odd
    def test_check_even_odd(self):
        self.assertEqual(check_even_odd(4), "Even")
        self.assertEqual(check_even_odd(7), "Odd")
        with self.assertRaises(TypeError):
            check_even_odd("a")

if __name__ == '__main__':
    # Run the unit tests and print the results
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestExercises))
