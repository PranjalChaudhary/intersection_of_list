input_list = [[5, 6, 8, 1, 4, 8, 1],
              [5, 5, 7, 6, 1],
              [5, 6, 9, 8, 8, 1]]

list1 = sorted(input_list, key=len, reverse=True)
min_list = list1.pop()

for array in list1:
    intersection = []
    for element in min_list:
        try:
            if array.index(element) >= 0:
                intersection.append(array.pop(array.index(element)))
        except ValueError:
            pass
    min_list = intersection

print(intersection)
