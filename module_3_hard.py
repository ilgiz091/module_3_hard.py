# сделал так, как подсказали на вебинаре, но получился каким-то громоздким.
def calculate_structure_sum(*data_structure, sum_list = []):
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            for j in i:
                if isinstance(j, int):
                    sum_list.append(j)
                if isinstance(j, str):
                    sum_list.append(len(j))
                else:
                    calculate_structure_sum(j)
        elif isinstance(i, dict):
            for j in i.values():
                if isinstance(j, int):
                    sum_list.append(j)
                if isinstance(j, str):
                    sum_list.append(len(j))
                else:
                    calculate_structure_sum(j)
            for j in i.keys():
                if isinstance(j, int):
                    sum_list.append(j)
                if isinstance(j, str):
                    sum_list.append(len(j))
                else:
                    calculate_structure_sum(j)
    return sum(sum_list)
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)


# Решение нашел в интернете, короткое решение, вроде бы и понятно, но в тоже время и непонятно.
def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

