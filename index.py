dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}


def merge_dict(dict_first, dict_second):
    arr=['감', '귤', '배', '사과', '포도']
    dict_total={}
    for i in arr:
        dict_total[i] = dict_first.get(i, 0) + dict_second.get(i, 0)
    print(dict_total)

merge_dict(dict_first, dict_second)