'''determine if a string has all unique characters.
followup: what if no additional data structures are allowed'''

input_strings = ['asdfasdf', 'asdfjkl']


def is_unique(input_string: str) -> bool:
    # sets only contain unique characters, so if the set is not the same length
    # it means duplicates were removed during creation of set
    string_set = set(input_string)
    return True if len(string_set) == len(input_string) else False

# what if no additional data structures are allowed?


def is_unique_brute_force(input_string: str) -> bool:
    # can iterate through the string and
    # search the string for duplicates
    for idx, character in enumerate(input_string):
        if character in input_string[idx+1:]:
            return False
    return True


# could sort the string, so duplicates would be side-by-side.
# then for each char, check the char immediately to the right.
# if it is the same, then return false:
# string = sorted(string) # this uses a list, so it's cheating
# for i in range(len(string)-2):
#   if string[i] == string[i+1]:
#       return False
# return True
