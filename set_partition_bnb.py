import time

import math

import psutil

def get_memory_usage():
    # Get the process ID
    pid = psutil.Process()

    # Get memory information
    memory_info = pid.memory_info()

    # Return the resident set size (RSS) in bytes
    return memory_info.rss


def partition_values_from_index(values, start_index, total_value, unassigned_value,
                                test_assignment, test_value, best_assignment, best_err):
    # Check if best_err[0] is already 0, and if so, exit the recursion
    if best_err[0] == 0:
        return
    
    # If start_index is beyond the end of the array,
    # then all entries have been assigned.
    if start_index >= len(values):
        # We're done. See if this assignment is better than
        # what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            # This is an improvement. Save it.
            best_err[0] = test_err
            best_assignment[:] = test_assignment[:]

            print(best_err[0])
            if best_err[0]==0:
                return
    else:
        # See if there's any way we can assign
        # the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value + values[start_index],
                                         best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value,
                                         best_assignment, best_err)





if __name__ == "__main__":
    txt_file_name = "d_80.txt"
    dataset = []

    # Open and read the text file
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            number = int(line.strip()) 
            dataset.append(number)
  
    start_time = time.time()
    before_memory = get_memory_usage()

    # Example usage:
    start_index = 0
    total_value = sum(dataset)
    unassigned_value = total_value
    test_assignment = [False] * len(dataset)
    test_value = 0
    best_assignment = [False] * len(dataset)
    best_err =  [float('inf')] # Using a list to simulate pass-by-reference for best_err

    partition_values_from_index(dataset, start_index, total_value, unassigned_value,
                                test_assignment, test_value, best_assignment, best_err)
    end_time = time.time()
    after_memory = get_memory_usage()

    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")

    memory_diff = after_memory - before_memory

    # Print the results in bytes
    print(f"Memory Before: {before_memory} bytes")
    print(f"Memory After:  {after_memory} bytes")
    print(f"Memory Diff:   {memory_diff} bytes")