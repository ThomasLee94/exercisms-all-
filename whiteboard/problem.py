def duplicate(list_num: [int])->bool:
    list_set=set(list_num)

    diff = list_num - list_set

    if diff:
        return True

    return False
