# this function returns True if the checking interval conflicts with the given interval
# and False otherwise
def is_in_range(tuple_to_check, range_tuple):
    if range_tuple[0] <= tuple_to_check[0] < range_tuple[1]:
        return True
    else:
        return False


def interval_partitioning(list_of_intervals):
    if len(list_of_intervals) == 0:
        raise ValueError("List of intervals cannot be empty")
    # ascending sort the interval_list by starting point using the sorted functions
    sorted_intervals = sorted(list_of_intervals, key=lambda x: x[0])

    current_partition = 1
    # 'partitions' is a dictionary where keys are the partition number and values are lists of intervals
    # the first sorted interval is always added to the first partition
    min_partitions = {current_partition: [sorted_intervals[0]]}

    # 'cannot_add_here' is a boolean that is True if we cannot add the current interval to the current partition
    # and False otherwise
    cannot_add_here = True

    # iterate from the second interval to the last interval
    for checking_interval in sorted_intervals[1:]:
        for partition, intervals in min_partitions.items():
            for current_interval in intervals:
                cannot_add_here = is_in_range(checking_interval, current_interval)
            # if the checking interval from the sorted interval list doesn't conflict with at least one of the
            # current intervals, then we can add it to the current partition
            if not cannot_add_here:
                min_partitions[partition].append(checking_interval)
                break
        # if we can not add the current interval to any partition, we create a new partition
        # and add the current interval to it
        if cannot_add_here:
            current_partition += 1
            min_partitions[current_partition] = [checking_interval]

    return min_partitions


def print_partitions(min_partitions):
    print(f"Minimum {len(min_partitions)} partition(s) required: ")
    for partition, intervals in min_partitions.items():
        print(f"Partition {partition}: {intervals}")
    print()


# Uncomment the following lines to test the code by direct tuple input
# interval_list = [(8, 13), (6, 9), (11, 14), (2, 7), (1, 7), (12, 20), (7, 13), (13, 20)]
# minimum_partitions = interval_partitioning(interval_list)
# print_partitions(minimum_partitions)
#
# interval_list2 = [(8, 12), (6, 9), (11, 14), (2, 7), (1, 7), (12, 20), (7, 12), (13, 19)]
# print_partitions(interval_partitioning(interval_list2))


# take input from the user and convert it to a list of tuples
interval_list = []
number_of_intervals = int(input("Enter the number of intervals: "))
print("Enter the intervals in the format: start end")
for i in range(number_of_intervals):
    interval = input(f"Enter interval {i + 1}: ").split()
    interval_list.append((int(interval[0]), int(interval[1])))
print_partitions(interval_partitioning(interval_list))
