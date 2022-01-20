# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

# For example:

#     # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                   must_start_with={"h", "y"})

def print_upper_words(words):
    """For a list of words, prints each word on a separate line, uppercased"""

    for word in words:
        print(word.upper())


def first_letter_e(words):
    """Only prints words that start with letter 'e' (upper or lowercase) """

    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

    # for word in words:
    #     if word.startswith("e") or word.startswith("E"):
    #         print(word.upper())


def print_word_starting_with_letter(words, starts_with):
    """Prints words that start with one of the passed in letters"""
    for word in words:
        for letter in starts_with:
            if word[0] == letter:
                print(word.upper())
                break

    # for word in words:
    #     for letter in starts_with:
    #         if word.startswith(letter):
    #             print(word.upper())
    #             break
