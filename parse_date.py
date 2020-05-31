import re

def parse_date(input):
    
    date_regex = re.compile(r'^(?P<day>[0-9]{2})[\.,/:](?P<month>[0-9]{2})[\.,/:](?P<year>[0-9]{4})$')
    matches = date_regex.search(input)
    # table = {"d":'day', "m":'month', "y":'year'}
    # print(matches.group(table))
    # print(matches.group('day','month','year'))

    # d = matches.group('day')
    # m = matches.group('month')
    # y = matches.group('year')
    # print("d: " + d + " m: " + m + " y: " + y)

    print(matches.groups())

parse_date("01.22.1991")
parse_date("01,22,1991")
parse_date("01/22/1991")
# parse_date("01,22,199134")