import re

def parse_bytes(input):
    data = re.compile(r'\d[0-1]*')
    return data.findall(input)


    # Approach with one input:

    # merged = data.search(input)
    # if merged:
    #     return merged.group()
    # return None


print(parse_bytes("01010101"))
print(parse_bytes("asahasa"))
print(parse_bytes("01010101 asahasa"))

