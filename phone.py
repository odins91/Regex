import re

def extract_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

# print(extract_phone("My numnber is 532 324-1234"))
# print(extract_phone("My numnber is 532 324-11123"))
# print(extract_phone("232 123-3342 asddawd"))
# print(extract_phone("532 324-1113"))

def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


# print(extract_all_phones("My numnber is 532 324-1234 or call me at 999 231-0000"))
# print(extract_all_phones("My numnber is 532 32-1234 or call me at 999 231-000"))


# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     else:
#         return False

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

print(is_valid_phone("342 234-2567"))
print(is_valid_phone("342 234-2567 asdad"))
print(is_valid_phone("342 234-25673 asdad"))