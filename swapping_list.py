import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]


titles.sort()
fixed_titles = []
# print(titles)

# to get one result:

# one_pattern = re.compile(r'^([\w ]+) \((\d{4})\)')
# first_result = one_pattern.sub("\g<2> - \g<1>", titles[1])
# print(first_result)

# first approach:

# pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
# for book in titles:
#     result = pattern.sub("\g<2> - \g<1>", book)
#     fixed_titles.append(result)
# fixed_titles.sort()
# print(fixed_titles)

# second approach:

sec_pattern = re.compile(r'^(?P<title>[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    sec_result = sec_pattern.sub("Book date = \g<date> - \g<title>", book)
    fixed_titles.append(sec_result)
fixed_titles.sort()
print(fixed_titles)