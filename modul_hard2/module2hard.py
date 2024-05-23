first_num = 9


list_ = list(range(first_num))
length = len(list_)

list_tmp = []
for i in range(20):
    for j in list_:
        if (i + j) % first_num == 0 and i < j:
            list_tmp.append(i)
            list_tmp.append(j)


print(*list_tmp)