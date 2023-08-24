# Prolog: Homework 3
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
"""
# supply program prolog (3 P's)
Purpose
Make a dictionary where a user can search, add, and remove definitons of a word
Pre-condition
User enters a number
Post-condition


· # main function
· # Display introductory message
· Your design here
"""
print("Welcome to My Dictionary! What can I do for you?")
print("1. Search for a word 2. Add a new word 3.Remove a word")
x = int(input("Please enter a number: "))
if x == 1:
  y = input("Enter the word you want to look up:")
  print(my_dict[y])
elif x == 2:
  z = input("Add the word you want: ")
  t = input("Please add a definition for it:")
  my_dict[z] = t

  for key, value in my_dict.items():
    print(key + ":" + value)

elif x == 3:
  j = input("Enter the word you want to remove: ")

  try:
    my_dict.pop(j)
    for key, value in my_dict.items():
        print(key + ":" + value + "\n")

    except: 
      print("uh typo? I don’t have this word in my database.")
      
import unittest


def main():

# initial dictionnary
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
# your code here 
# Enter 

print("Welcome to My Dictionary! What can I do for you?")
print("1. Search for a word 2. Add a new word 3.Remove a word")
x = int(input("Please enter a number: "))
if x == 1:
  y = input("Enter the word you want to look up:")
  print(my_dict[y])
elif x == 2:
  z = input("Add the word you want: ")
  t = input("Please add a definition for it:")
  my_dict[z] = t

  for key, value in my_dict.items():
    print(key + ":" + value)

elif x == 3:
  j = input("Enter the word you want to remove: ")

try:
  my_dict.pop(j)
    for key, value in my_dict.items():
        print(key + ":" + value + "\n")

  except: 
    print("uh typo? I don’t have this word in my database.")

# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_word_success(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = test_dict["Variable"]
    expected = lookup_word(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_search_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = "N/A"
    expected = lookup_word(test_dict, "Array")
    self.assertEqual(actual, expected)

  def test_add_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Array":
      "an arrangement of a series of terms according to value, as from largest to smallest.",
    }
    expected = add_word_to_dict(
      test_dict, "Array",
      "an arrangement of a series of terms according to value, as from largest to smallest."
    )

    self.assertEqual(actual, expected)

  def test_add_word_duplicate(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Variable(2)": "temporary value assignment"
    }
    expected = add_word_to_dict(test_dict, "Variable",
                                "temporary value assignment")
    self.assertEqual(actual, expected)

  def test_delete_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = {}
    actual = delete_in_dict(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = test_dict
    actual = delete_in_dict(test_dict, "Array")
    self.assertEqual(actual, expected)


#uncomment to run tests
# unittest.main()

main()
