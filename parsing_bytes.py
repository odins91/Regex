import re

def parse_bytes(input):
    # Approach with many inputs in the line:
    # data = re.compile(r'\b\d[0-1]{7}\b')
    # return data.findall(input)

    # Second approach:
    # binary_regex = re.compile(r'\b[01]{8}\b')
    # results = binary_regex.findall(input)
    # return results


    # Approach with one input in the line:
    binary_regex = re.compile(r'\b[01]{8}\b')
    merged = binary_regex.search(input)
    if merged:
        return merged.group()
    return None


print(parse_bytes("01010101"))
print(parse_bytes("asahasa"))
print(parse_bytes("01010101 asahasa"))

