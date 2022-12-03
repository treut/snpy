import datetime as d


def date_in_future(days = None):
    if type(days) is not int:
        days = 0
    return d.datetime.fromtimestamp(d.datetime.now().timestamp() + (days * 86400)).strftime("%d-%m-%Y %H:%M:%S")


print(date_in_future([]))
print(date_in_future(2))

print(date_in_future(45))
print(date_in_future(149))
print(date_in_future())
print(date_in_future('dfsdfsdfsdf'))
