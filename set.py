def intersection(input_list):
    set_list = list(map(set, input_list))
    intersections = set_list[0]
    for sets in set_list:
        intersections = sets.intersection(intersections)

    # print(intersections)
    intersections = list(intersections)
    freq_dict = {}
    for array in input_list:
        for element in intersections:
            count = array.count(element)
            if freq_dict.get(element, 0) == 0:
                freq_dict[element] = count
            else:
                freq_dict[element] = min(count, freq_dict[element])
    output = []
    for key, value in freq_dict.items():
        for i in range(value):
            output.append(key)
    print(sorted(output))


list1 = [[5, 5, 5, 8, 10, 9],
         [5, 5, 7, 8, 9],
         [5, 5, 8, 9, 11]]
intersection(list1)
