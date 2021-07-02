'''given a string and its length, strip out trailing spaces and replace spaces with %20'''

test_case = 'this is a test   '


def urlify(string: str) -> str:
    return string.rstrip().replace(' ', '%20')
