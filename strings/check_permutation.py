'''given two strings, check if one is a permutation of the other'''

string_pairs = [('asdf', 'fdsa'), ('asdf', 'jkl;')]


def check_permutations(string_pair: tuple) -> bool:
    # permutation: one string has all the characters that are in another string
    # also, the length of both strings are the same
    # fails on this case: ('asdff', 'fdsaa')
    string1, string2 = string_pair
    if len(string1) == len(string2):
        for char in string1:
            if char not in string2:
                return False
        return True
    return False


def check_permutations2(string_pair: tuple) -> bool:
    # working, and much simpler
    string1, string2 = string_pair
    if sorted(string1) == sorted(string2):
        return True
    return False
