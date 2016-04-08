
# import random
# from random import randint
def insertion(arr):
	# look at all values in arr
    for i in range(0,len(arr)):
    # set minimum equal to the first value
        minimum = i
    # start comparing from the second value
        for j in range(i, len(arr)):
    # set a new minimum if we find a value thats lower than our initial value
            if arr[j] < arr[minimum]:
                minimum = j
    # use a temp variable to store data to make the switch
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp

    return arr

arr = [4,3,1,5,2,10,12,56,23,11,12]

print insertion(arr)