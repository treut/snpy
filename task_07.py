def combine_anagrams(words_array):
    result = {}
    for k, v in enumerate(words_array):
        conv = "".join(sorted(list(str(words_array[k]).lower())))

        if conv not in result.keys():
            result[conv] = []
        result[conv].append(words_array[k])
    return list(result.values())


example = ["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]

print(combine_anagrams(example))
