import re

def censor(input):
    pattern = re.compile(r'\bFrack\w* [a-z]+', re.IGNORECASE)
    # result = pattern.sub("\g<1> CENSORED \g<2>", input)
    result = pattern.sub("CENSORED", input)
    # result = pattern.sub("\g<1> CENSORED", input)
    # result = pattern.search(input)
    return result
    

print(censor("Fracking You"))
print(censor("I Frack uu donw"))
print(censor("I hope You"))
print(censor("Frack Frack"))