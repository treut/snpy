import re


def multiply_numbers(inputs = None):
    inputs = re.sub(r'[^0-9]', "", str(inputs))
    if inputs == "":
        return None
    else:
        inputs = list(inputs)
        res = int(inputs[0])
        for k, v in enumerate(inputs):
            if k == 0:
                continue
            res *= int(v)
        return res


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
