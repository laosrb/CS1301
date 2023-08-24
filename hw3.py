# Prolog: Homework 3
# Author:  Ryan Bouapheng
# Email:  rbouapheng1@student.gsu.edu
# Section: 004, CSC1301 
"""
# supply program prolog (3 P's)                                                             # FINISH THIS I DIDN"T FINISH THINDDJSSfjpdslakjf;lkjf
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
import unittest
def main():
# prompt
  print("   ***  dictionary  ***")                                
  print('''Welcome to My Dictionary! What can I do for you?
   1. Search for a word                                           
   2. Add a new word
   3. Remove a word''')
# initial dictionary
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
  user_input = int(input("Please type your choice number: "))     # user input

  x = int(input("Please enter a number: "))                       # Asks the user for an input
  if x == 1:                                                      # searches for a word
    y = input("Enter the word you want to look up:")
    print(my_dict[y])

  elif x == 2:
    new_word = input("Add the word you want: ")                   # input the word to be added
    definiton = input("Please add a definition for it:")
    my_dict[new_word] = definiton                                 # makes the input = the defintion

    for key, value in my_dict.items():
      print(key + ":" + value + "\n")

  elif x == 3:
    j = input("Enter the word you want to remove: ")

    try:

      my_dict.pop(j)                                            # removes the word

      for key, value in my_dict.items():
        print(key + ":" + value + "\n")

    excepted = print("uh typo? I don’t have this word in my database.")

  print("Thanks for using MyDictionary.")
  
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
