def coincidence(array=None, ranges=None):
    if array is None or ranges is None:
        return []
    else:
        result = []
        for i in array:
            if type(i) is int or type(i) is float:
                if ranges.start <= i <= ranges.stop-1:
                    result.append(i)
        return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
