import sys
import numpy as np

# Adding a comment
def get_smallest_non_negative_difference_set(list_1, list_2):
    # Sorting the arrays so that the data will be on ascending order.
    list_1.sort()
    list_2.sort()

    # We need the get the smallest non-negative numbers.
    # So filtering the input arrays to remove any non-negative numbers.
    filtered_list_1 = [element for element in list_1 if element > 0]
    filtered_list_2 = [element for element in list_2 if element > 0]

    # Get the length of the filtered arrays.
    list_1_length = len(filtered_list_1)
    list_2_length = len(filtered_list_2)

    # Assign a sys max value to a variable.
    # Now iterate through the both arrays and find the difference.
    # If the difference is lesser than previously stored result, assign it as new result.
    # Keep repeating this until we find the smallest.
    result = sys.maxsize
    smallest_element_from_list_1 = None
    smallest_element_from_list_2 = None
    result_list = []

    # Instantiating the variables for the while loop
    i = 0
    j = 0

    while i < list_1_length and j < list_2_length:
        difference = abs(filtered_list_1[i] - filtered_list_2[j])

        if difference == result:
            result_list.append([filtered_list_1[i], filtered_list_2[j]])

        if difference < result:
            result = difference
            smallest_element_from_list_1 = filtered_list_1[i]
            smallest_element_from_list_2 = filtered_list_2[j]
            if result_list is not None:
                result_list.clear()

            result_list.append([smallest_element_from_list_1, smallest_element_from_list_2])

        if filtered_list_1[i] < filtered_list_2[j]:
            i += 1
        else:
            j += 1

    print(result_list)


# Another way to Question - 1
# This method assume that we don't more than one pair where there it has same difference.
# PS: I did not add those pairs into another list like I have in the other function.
def get_non_negative_difference(list_1, list_2):
    list_1.sort()
    list_2.sort()

    filtered_list_1 = [ele for ele in list_1 if ele > 0]
    filtered_list_2 = [ele for ele in list_2 if ele > 0]

    result = None
    difference = sys.maxsize

    for idx, x in enumerate(filtered_list_1):
        list_1_index = idx
        list_1_value = x
        for i in range(list_1_index, len(filtered_list_2)):
            list_2_value = filtered_list_2[i]
            difference_value = abs(list_1_value - list_2_value)
            if difference_value < difference:
                difference = difference_value
                result = [list_1_value, list_2_value]

    return result


def get_randon_arrays_of_integers():
    # Using the numpi
    return np.random.randint(1, 1000000, size=(2, 1000))


if __name__ == "__main__":
    list_eg_1_1 = [5, 8, 10, 20]
    list_eg_1_2 = [1, 3, 6, 9, 13, 19]
    get_smallest_non_negative_difference_set(list_eg_1_1, list_eg_1_2)
    print(get_non_negative_difference(list_eg_1_1, list_eg_1_2))

    list_eg_2_1 = [5, 8, 10, 19]
    list_eg_2_2 = [1, 3, 12, 20]
    get_smallest_non_negative_difference_set(list_eg_2_1, list_eg_2_2)
    print(get_non_negative_difference(list_eg_2_1, list_eg_2_2))

    random_integer_arrays = get_randon_arrays_of_integers()
    random_integer_list_1 = random_integer_arrays[0]
    random_integer_list_2 = random_integer_arrays[1]
    get_smallest_non_negative_difference_set(random_integer_list_1, random_integer_list_2)





# Question 3:
#     1: Numpi,
#     2: Pandas
#     3: spark
