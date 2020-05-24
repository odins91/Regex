import re

def valid_time(input):
    aline = re.compile(r'^\d{1,2}:\d{2}$')
    correct = aline.search(input)
    if correct:
        return True
    return False

print(valid_time("12:23"))
print(valid_time("3:23"))
print(valid_time("3:23"))
print(valid_time("323:01"))
print(valid_time(" is it 23:01"))
print(valid_time("23:01 hehe"))