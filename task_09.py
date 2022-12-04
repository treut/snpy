def delete_less10(dict_in):
    dict_out = {}
    for k, v in dict_in.items():
        if v >= 10:
            dict_out[k] = v
    return dict_out


def result_unite(dict1, dict2):
    result = dict1
    for k, v in dict2.items():
        if k not in result:
            result[k] = v
    return result


def connect_dicts(dict1, dict2):
    if (sum(dict1.values()) == sum(dict2.values())) or (sum(dict1.values()) < sum(dict2.values())):
        result = result_unite(delete_less10(dict2), delete_less10(dict1))
    else:
        result = result_unite(delete_less10(dict1), delete_less10(dict2))
    return dict(sorted(result.items(), reverse = True))


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
