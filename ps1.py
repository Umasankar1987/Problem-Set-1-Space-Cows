###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    itemsCopy = sorted(cows.items(),key = lambda cows: cows[1], reverse = True)
    total_result = []
    while itemsCopy and itemsCopy[-1][1] < limit:
        result = []
        totalWeight = 0.0
        for i in itemsCopy.copy():
            if (totalWeight + i[1]) <= limit:
                result.append(i[0])
                totalWeight += i[1]
                itemsCopy.remove(i)
        total_result.append(result)
    return total_result    
    pass


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    itemcopy1 = {i:j for i,j in cows.items() if j <= limit}

    trips = []
    for partition in get_partitions(itemcopy1):
        flag = True  
        for trip in partition:
            if sum(map(itemcopy1.get, trip)) > limit:
                flag = False
                break
        if flag:
            if len(partition) < len(trips) or len(trips) == 0:
                trips = partition
    return trips
       
                
        
    pass

        
# Problem 3
def compare_cow_transport_algorithms(cows, limit = 10):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    
    

    greedy_start = time.time()  
    greedy_result = greedy_cow_transport(cows)
    greedy_end = time.time()  
    print('--- Greedy algorithm ---')
    print('{:.4f} ms'.format((greedy_end-greedy_start)*1000))
    print()

    brute_start = time.time()  
    brute_result = brute_force_cow_transport(cows)
    brute_end = time.time()  
    print('--- Brute force algorithm ---')
    print('{:.4f} ms'.format((brute_end -brute_start)*1000))

    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""


cows = load_cows("ps1_cow_data.txt")
limit= 10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
print(compare_cow_transport_algorithms(cows,limit))


