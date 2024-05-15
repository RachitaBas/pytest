
# test_calculator.py
# import pytest

# def test_add():
#     assert 1+2 == 3

# def test_add_negative():
#     assert 4+5 == 9

# def test_subtraction():
#     num1,num2 = 2,3
#     assert num1 - num2 == -1


# def test_string_uppercase(): #Test function to check if a string is in UPPERcase
#     uppercase_string ="HELLO"
#     assert uppercase_string.isupper()

# def test_string_lowercase():   #Test function to check if a string is in lowercase
#     lowercase_string = "hEllo"
#     assert lowercase_string.islower()

 # 
# Test function to check if a string is alphanumeric
# def test_string_alphanumeric():  
#         test_string_alphanumeric = "Hello"
        # assert test_string_alphanumeric.isalnum()

# def test_function_inequality():
#     string1 = "Hello"
#     string2 = "Hello"
#     assert string1 == string2

# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_equal_strings(self):
#         string1 = "Hello"
#         string2 = "Hello"
#         self.assertEqual(string1, string2)

#     def test_not_equal_strings(self):
#         string1 = "Hello"
#         string2 = "World"
#         self.assertNotEqual(string1, string2)

import unittest  # will execute the test methods and report whether each test passed or failed.

def add(a,b):
     return a + b 

#creating test case class
class TestAddition(unittest.TestCase):  #We create a test case class TestAddition that inherits from unittest.TestCase.

    def test_add_positive_numbers(self):
        self.assertEqual(add(9,2),11)

# if __name__ == '__main__':
#     unittest.main()   #unittest.main() to run the tests when the script is executed directly.

