import re
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
# print(pattern.findall(text))
# print(pattern.search(text).group())

result = pattern.sub("REDACTED", text)
print(result)

result2 = pattern.sub("\g<1> RED", text)
print(result2)

result3 = pattern.sub("\g<1> \g<2> BLUE", text)
print(result3)