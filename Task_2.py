# Дополниетельная задача

lst_num = list(map(int, input().split()))
lst = []
for i in lst_num:
    if lst_num.count(i) == 1:
        lst.append(i)
print(*lst)
