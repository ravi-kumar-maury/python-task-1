from numpy import concatenate, sort


list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]

def funcc(x):
    return x['id']

def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    # list_2.sort()
    mergedraw = concatenate([list_1, list_2])
    mergedraw =sorted(mergedraw, key=funcc)
    # mergedraw.sort(key=funcc)
    skipnext = False
    mergedlist = []
    for i in range(len(mergedraw)):
        if skipnext:
            skipnext = False
        elif i+1==len(mergedraw):
            mergedlist.append(mergedraw[i])
        elif (mergedraw[i]['id']== mergedraw[i+1]['id']):
            mergedlist.append(dict(mergedraw[i] | mergedraw[i+1]))
            # print(mergedraw[i] | mergedraw[i+1])
            skipnext = True
        else:
            mergedlist.append(mergedraw[i])
    return mergedlist


list_3 = merge_lists(list_1, list_2)
print(list_3)
