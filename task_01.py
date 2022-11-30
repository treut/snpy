import re


def is_palindrome(string):
    string = re.sub(r'[ \-,.\'\"!]', "", str(string).lower())
    rev = list(string)
    rev.reverse()
    return "".join(rev) == string


examples = ["A man, a plan, a canal -- Panama", "Madam, I'm Adam!", 333, None, "Abracadabra"]
for i in examples:
    print(is_palindrome(i))
