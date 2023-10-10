# write a program witch takes at least 5 minimum words (use only 1 input) separated by comma . 
# From those words , make a dictionary where the key is a letter and value is a number of the frequency the letter did appear in all those words. 
# Letters should be in alphabetical order. Everything should be done thorugh github workflow.

import re

five_word_input = input("Enter five words separated by comma: ")
five_word_input = re.sub(" ","", five_word_input)
list_of_words = five_word_input.split(",")
word_counter = len(list_of_words)

if word_counter < 5:
    print("You've entered less than five words.")
    exit(1)

letters_list = []

for word in list_of_words:
    letters_list.extend(word.lower())

unique_letters_set = sorted(set(letters_list))

my_dictionary = {}
for item in unique_letters_set:
    my_dictionary[item] = letters_list.count(item)
print(f"Result is: {my_dictionary}")