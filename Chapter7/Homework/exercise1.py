# 自定义求最大值的函数
def index_max(number_list):
    max_number = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > max_number:
            max_number = number_list[i]
    print(number_list.index(max_number))

list1 = [5, 8, 2, 1, 9, 3, 6, 7]
index_max(list1)

