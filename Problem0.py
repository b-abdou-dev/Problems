
# accessing list values based on given list indexes
index_list = [1, 5, 8, 9, 10, 2]
access_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
def afunction(i):
    arg_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
    return arg_list[i]

def my_pickups(fun, list):
    result = []
    for i in list:
        result.append(fun(i))
    return result
print("List of indexes to be accessed is:", index_list)
print("List to be accessed is", access_list)
print("returned list ", my_pickups(afunction, index_list))

