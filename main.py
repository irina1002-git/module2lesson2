my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_number = 0
while current_number < len(my_list):
    if my_list[current_number] > 0:
        print(my_list[current_number])
        current_number += 1
    elif my_list[current_number] == 0:
        current_number += 1
    else:
        continue
