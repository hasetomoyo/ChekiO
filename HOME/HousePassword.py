import sys

def checkio(data):

    upp_result = low_result = alp_result = num_result = False

    if len(data) < 10:
        return False

    for v in data:
        if v.isupper():
            upp_result = True
        if v.islower():
            low_result = True
        if v.isalpha():
            alp_result = True
        if v.isdecimal():
            num_result = True

    if upp_result and low_result and alp_result and num_result:
        return True
    else:
        return False

print(checkio('1aA'))
