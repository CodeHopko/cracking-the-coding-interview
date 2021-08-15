'''given a string, determine if it is a permutation of a palindrome. ignore non-letter characters'''

# palindrome: same spelling forwards and backwards. so string == reversed(string)
# assume letters are scrambled so string == reversed(string) will not suffice
# need every character to have a duplicate
# Exception: one character can be without duplicate if it is in the middle.

# Strategy:
#   strip out all non-letter characters
#   check every character to see if it has a duplicate
#   allow one duplicate: counter variable. if > 1, return false
#   if iterated through list and counter <= 1, then return true

test_strings = ['asdffdsa', 'asdfjkls']


def permutation_of_palindrome(string: str) -> bool:
    # TODO: strip all non-letter characters. Use some regex...
    unique_count = 0
    for char in set(string):
        if string.count(char) % 2 == 1:
            unique_count += 1
        if unique_count > 1:
            return False
    return True
