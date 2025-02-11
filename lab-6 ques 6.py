def sort_by_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])

# Example usage
tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (3, 1)]
sorted_tuples = sort_by_last_element(tuples)
print("Sorted list of tuples by the last element:", sorted_tuples)
