import unittest
def lookup_word(my_dict, word_1):                    # I had to define these fuctions before the main because it didn't work
        print("")                                    
        if word_1 in my_dict:
          return my_dict[word_1]                     # You have to return the dictionary's word's defintion and not print it out b/c that's something else
        else: 
          return "N/A"
def add_word_to_dict(my_dict, word_2, user_definition):
    if word_2 in my_dict:                           # To add a new word word in my dictionary I have to 
      new_word = word_2 + "(2)"
      my_dict[new_word] = user_definition
    else:
      my_dict[word_2] = user_definition
    return my_dict
def delete_in_dict(my_dict, word_3):
    if word_3 in my_dict:
        del my_dict[word_3]
    return my_dict
"""
My wrong attempt for creating the look up function
# TypeError: 'int' object is not callable for lookup_word(my_dict,lookup_word)
def lookup_word(my_dict,lookup_word):   # the parameters of lookup_word are the dictionary my_dict and the user input of lookup_word variable
  if lookup_word in my_dict:            # the lookup_word is the user input when they put 1 in variable user_input  # my_dict is the dictionary with keys of the names and values are the definition
    return my_dict[lookup_word]         # the key is variable lookup_word so if the lookup_word = Variable if it is in my_dict then it will return the definiton of key variable
  else:                                 # lookup_word is a key
    print()"""

def main():
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
  print("   ***  dictionary  ***")                                # prompt
  print('''Welcome to My Dictionary! What can I do for you?
   1. Search for a word                                           
   2. Add a new word
   3. Remove a word''')
  user_input = int(input("Please type your choice number: "))
  print()
  if user_input == 1:                                           # if user types in 1
    word_ = input("Enter the word you want to look up: ")
    if word_ in my_dict:                                    
      print(word_ + ":", lookup_word(my_dict, word_))
    else:
      print(lookup_word(my_dict, word_))
    print()
    print("Thanks for using MyDictionary.")
    print()
  elif user_input == 2:                                         # if user types in 1
    word_2 = input("Enter the word you want to add: ")
    user_definition = input("Please add a definition for it: ")

    add_word_to_dict(my_dict, word_2, user_definition)
    print("Here's all the words I have: ")

    for key, value in my_dict.items():
        print(key, ':', value)
    print()
    print("Thanks for using MyDictionary. ")
    print()
  elif user_input == 3:                                         # if user types in 1
    word_3 = input("What word do you want to remove? ")
    if word_3 in my_dict:
      delete_in_dict(my_dict, word_3)
      print(word_3, "is removed.")
      print("Here's all the words I have: ")
      for key, value in my_dict.items():
        print(key, ':', value)
      print()
    elif word_3 not in my_dict:
      print("up typo? I don't have this word in my database.")
  else:
    print("Please pick another number among 1, 2, 3.")
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
unittest.main()
main()
