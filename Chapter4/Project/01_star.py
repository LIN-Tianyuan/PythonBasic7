"""
for number in range(1, 10):
    print(number * '*')
"""
"""
for number in range(9):
    print('*', end="")
"""

# Row
for i in range(1, 10):
    # Column
    for j in range(i):
        print('*', end="")
    print()
