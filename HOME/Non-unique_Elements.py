def checkio(data):

    check_data = {}
        
    for k in data:
        check_data.setdefault(k, 0)
        check_data[k] = check_data[k] + 1
    print(check_data)

    delte_obj = []
    for k, v in check_data.items():
        if v == 1:
            delte_obj.append(k)
    print(delte_obj)

    result_data = []
    for k in data:
        if k not in delte_obj:
            result_data.append(k)

    return result_data

print(checkio([1, 2, 3, 4, 5]))