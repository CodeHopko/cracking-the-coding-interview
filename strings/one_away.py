'''given a pair of strings, check if they are one away from each other. Either one insertion, deletion, or update away'''

input_str = [('pale', 'pal'), ('pales', 'pale'),
             ('pale', 'bale'), ('pale', 'bake')]

# insertion:
#   diff b/t length == 1
#   character is in the other string, but may have an offset of up to 1
#       char in string2[idx-1:idx+1]
#       there may be one character that does not follow this rule

# deletion
#   diff b/t length == 1
#   character is in the other string, but may have an offset of up to 1
#       char in string2[idx-1:idx+1]

# update
#   diff b/t length == 0
#   every char is in the other string at string2[idx]
#       except for one


def one_away(string_pair: tuple) -> bool:
    string1, string2 = string_pair
    diff_len = abs(len(string1) - len(string2))
    unique_count = 0

    if diff_len > 1:
        return False

    elif diff_len == 0:
        # potential update
        for idx, char in enumerate(string1):
            if char not in string2[idx]:
                unique_count += 1
            if unique_count > 1:
                return False

    elif diff_len == 1:
        # potential insertion/deletion
        for idx, char in enumerate(string1):
            if idx == 0:
                if char not in string2[0:idx+1]:
                    unique_count += 1
            elif char not in string2[idx-1:idx+1]:
                unique_count += 1
            if unique_count > 1:
                return False
    return True
