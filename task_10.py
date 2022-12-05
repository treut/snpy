import re


def count_words(string_ex):
    result = {}
    string_ex = re.split(r'([a-zа-я]+)', str(string_ex).lower())
    for k, v in enumerate(string_ex):
        if re.sub(r'[^a-zа-я]', "", v) == "":
            continue
        result[v] = result.get(v, 0) + 1

        #v1.0
        # if v not in result.keys():
        #     result[v] = 0
        # result[v] += 1

    return result


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
print(count_words("A man, a plan, a canal -- Panama тест текст тест тест"))
