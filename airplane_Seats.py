input = [[1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
group1 = [0, 1, 2]
group2 = [3, 4, 5, 6]
group3 = [7, 8, 9]


def findPlaceInFlight(num):
    lis = []
    for row in range(0, 2):
        check_group1(row, lis, num)  # group1
        check_group2(row, lis, num)  # group2
        check_group3(row, lis, num)  # group3

    return lis


def check_group1(row, lis, num):
    collect = []
    # Group1
    for g1 in group1:
        print str(row) + "_" + str(g1)
        arr = input[row]
        if arr[g1] == 0:
            collect.append(str(row) + str(g1))
        else:
            return

    if len(collect) == num:
        top = ()
        for ele in collect:
            top = top + (ele,)
        lis.append(top)


def check_group2(row, lis, num):
    collect = []
    # Group2
    for g2 in group2:
        if len(collect) == num:
            top = ()
            for ele in collect:
                top = top + (ele,)
            lis.append(top)
            collect.pop(0)
        arr = input[row]
        if arr[g2] == 0:
            collect.append(str(row) + str(g2))

    if len(collect) == num:
        top = ()
        for ele in collect:
            top = top + (ele,)
        lis.append(top)


def check_group3(row, lis, num):
    collect = []
    # Group3
    for g3 in group3:
        arr = input[row]
        if arr[g3] == 0:
            collect.append(str(row) + str(g3))
        else:
            return

    if len(collect) == num:
        top = ()
        for ele in collect:
            top = top + (ele,)
        lis.append(top)


out = findPlaceInFlight(3)
print out
