def get_minimum(data):
    minimum = data[0]
    minimum_index = 0

    for index, value in enumerate(data):
        if value < minimum:
            minimum = value
            minimum_index = index
    return minimum, minimum_index


def selection_sort(data):
    for index in range(len(data)):
        minimum, minimum_index = get_minimum(data[index:])

        data[minimum_index + index] = data[index]
        data[index] = minimum
    return data
