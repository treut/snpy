def merged(listr):
    result = []
    for i in listr:
        if type(i) is list or type(i) is tuple:
            result.extend(merged(i))
        elif type(i) is int or type(i) is float:
            result.append(int(i))
    return result


def max_odd(array):
    result = []
    for i in merged(array):
        if i % 2:
            result.append(i)
    if not len(result):
        return None
    else:
        return max(result)


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))

#tuple
# print(max_odd(['ololo', 2, 3, 4, (1, 5, [7, 9, 4]), None]))
