def my_max(n1, n2, n3):
    max_number = n1
    if n2 > max_number:
        max_number = n2
    if n3 > max_number:
        max_number = n3
    return max_number

number = my_max(6, 18, 4)
print(number)