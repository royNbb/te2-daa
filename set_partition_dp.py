import time
import psutil
'''
source code: https://www.geeksforgeeks.org/partition-problem-dp-18/
'''

def get_memory_usage():
    # Get the process ID
    pid = psutil.Process()

    # Get memory information
    memory_info = pid.memory_info()

    # Return the resident set size (RSS) in bytes
    return memory_info.rss


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
 
    return part[sum // 2][n]
 
 
 
# Driver code
if __name__ == "__main__":
    txt_file_name = "d_10.txt"
    dataset = []

    # Open and read the text file
    with open(txt_file_name, 'r') as txt_file:
        for line in txt_file:
            number = int(line.strip()) 
            dataset.append(number)

    print(dataset)
    print(len(dataset))

    start_time = time.time()
    before_memory = get_memory_usage()

    # Function call
    result = findPartition(dataset, len(dataset))

    if result == True:
        print("Can be divided into two subsets of equal sum")
    else:
        print("Can not be divided into two subsets of equal sum")

    end_time = time.time()
    after_memory = get_memory_usage()


    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"Elapsed time: {elapsed_time_ms:.2f} milliseconds")


    memory_diff = after_memory - before_memory

    # Print the results in bytes
    print(f"Memory Before: {before_memory} bytes")
    print(f"Memory After:  {after_memory} bytes")
    print(f"Memory Diff:   {memory_diff} bytes")