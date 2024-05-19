def average(*args):
    len_ = len(args)
    sum_ = 0
    for val in args:
        sum_ += val
    return sum_ / len_


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_mean = [average(*v) for v in grades]
stud = sorted(list(students))
dict_ = {k: v for k, v in zip(stud, list_mean)}
print(dict_)
