def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(have_common_member(list1,list2))
