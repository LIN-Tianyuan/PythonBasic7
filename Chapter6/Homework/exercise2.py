number_list = [32, 5, 12, 8, 3, 75, 2, 15]
# number_list = [-1, -2, -3, -4, -5, -6]
max_number = number_list[0]
for i in range(len(number_list)):
    if max_number < number_list[i]:
        max_number = number_list[i]
print(max_number)

