import re

def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.groups())
    print(matches.group(1))
    print(matches.group('first'))
    print(matches.group('last'))
    print(matches.group('first','last'))

parse_name("Mrs. Tidla swinton")