def sort_list(list = None):
    if list is None or list == []:
        return []
    else:
        mini = min(list)
        maxi = max(list)

        for k, v in enumerate(list):
            if v == mini:
                list[k] = maxi
            elif v == maxi:
                list[k] = mini
        list.append(mini)
        return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
