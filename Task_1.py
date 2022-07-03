# Обязательная задача

lst_num = list(map(int, input().split()))
lst_2 = []
for i in lst_num:
    if i % 3 == 0 and i % 5 != 0:
        lst_2.append(i)
print(max(lst_2), min(lst_2))
print(lst_2)
