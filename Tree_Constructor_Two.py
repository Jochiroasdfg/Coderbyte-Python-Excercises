from collections import Counter


def TreeConstructor(strArr):
    parent = []
    child = []

    for i in strArr:
        child.append(int(i[1]))
        parent.append(int(i[3]))
    # each parent node have at most 2 children
    for k, v in Counter(parent).items():
        if v > 2:
            return False
    # each node is unique
    for k, v in Counter(child).items():
        if v > 1:
            return False
    return True


print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))
