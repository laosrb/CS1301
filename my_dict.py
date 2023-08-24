# Prolog: Homework 3
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
"""
# supply program prolog (3 P's)                                                     # FINISH THIS I DIDN"T FINISH THINDDJSSfjpdslakjf;lkjf
Purpose
Make a dictionary where a user can search, add, and remove definitons of a word
Pre-condition
User enters a number
Post-condition


· # main function
· # Display introductory message
· Your design here
"""
import unittest                         # TypeError: 'int' object is not callable for lookup_word(my_dict,lookup_word)
def lookup_word(my_dict,lookup_word):   # the parameters of lookup_word are the dictionary my_dict and the user input of lookup_word variable
  if lookup_word in my_dict:            # the lookup_word is the user input when they put 1 in variable user_input  # my_dict is the dictionary with keys of the names and values are the definition
    return my_dict[lookup_word]         # the key is variable lookup_word so if the lookup_word = Variable if it is in my_dict then it will return the definiton of key variable
  else:                                 # lookup_word is a key
    return "N/A"
def add_work_to_dict(my_dict):
  print()

def main():

# initial dictionnary
  my_dict = {
    "Variable":                                                   # key variable :
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
# your code here 
# Enter 

  # lookup_word = ''
  add_word_to_dict = 0
  delete_in_dict = 0
  print("   ***  dictionary  ***")                                # prompt
  print('''Welcome to My Dictionary! What can I do for you?
   1. Search for a word                                           
   2. Add a new word
   3. Remove a word''')
  user_input = int(input("Please type your choice number: "))     # user input
  print("\n")
  definition = {
      "a quantity or function that may assume any given value or set of values."
  }
  if user_input == 1:                                             # look up function
      lookup_word = input("Enter the word you want to look up: ")     # we are trying to search for the input of the variable lookup_word
      if key in my_dict:

      print(my_dict[lookup_word,])
      """lookup_word(my_dict,lookup_word)
      print(lookup_word, my_dict[lookup_word])"""
      for key, value in dict:

        print()
  if user_input == 2:                                             # add function
      add_word_to_dict = input("Enter the word you want to add: ")
  if user_input == 3:                                             # remove function
      delete_in_dict = input("Enter the word you want to remove: ")
      delete_in_dict.pop
      delete_in_dict.index
  print("Here's all the words I have: ")

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
    expected = lookup_word(test_dict, "Array")                # f
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
