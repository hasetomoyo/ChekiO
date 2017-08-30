def checkio(text):

    text = text.lower()

    count = {}
    for k in text:
        count.setdefault(k, 0)
        count[k] += 1

    max_value = 0
    for k, v in count.items():
        if k.isalpha():
            if v > max_value:
                max_value = count[k]
                max_value_key = []
                max_value_key.append(k)
            elif v == max_value:
                max_value_key.append(k)

    max_value_key.sort()
    return max_value_key[0]


print(checkio('Hello Woeorlrrd!!!!!!!!!!!'))