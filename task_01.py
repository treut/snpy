import re


def is_palindrome(string):
    string = re.sub(r'[^0-9a-zа-я]', "", str(string).lower())
    return string == string[::-1]

    #v1.0
    # rev = list(string)
    # rev.reverse()
    # return "".join(rev) == string


examples = ["A man, a plan, a canal -- Panama", "Madam, I'm Adam!", 333, None, "Abracadabra", "А-=з^%А@#З$а", "Ол**=-оЛ&^&%^оло"]
for i in examples:
    print(is_palindrome(i))
