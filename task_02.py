def coincidence(array=None, ranges=None):
    if array is None or ranges is None:
        return []
    else:
        result = []
        rangeres = []
        for i in ranges:
            rangeres.append(i)
            rangeres.append(i + 0.5)
        for b in array:
            if b in rangeres:
                result.append(b)
        return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
