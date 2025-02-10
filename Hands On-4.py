#Problem 1

def merge_two_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    
    merged_array = arrays[0]
    for i in range(1, len(arrays)):
        merged_array = merge_two_arrays(merged_array, arrays[i])
    
    return merged_array

#Prove the time complexity of the algorithms:

import time
import random

def generate_sorted_arrays(K, N, max_val=1000):
    arrays = []
    for _ in range(K):
        array = sorted(random.sample(range(max_val), N))
        arrays.append(array)
    return arrays

def merge_two_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def merge_k_sorted_arrays_iterative(arrays):
    total_merge_operations = 0  
    merged_array = arrays[0]  
    
    for i in range(1, len(arrays)):
        arr1 = merged_array
        arr2 = arrays[i]
        total_merge_operations += len(arr1) + len(arr2)  
        merged_array = merge_two_arrays(arr1, arr2)
    
    return merged_array, total_merge_operations

#Comment on way's you could Improve your Implementation:

#I could have reduced time complexity by using a different approach. I could've used an approach that merged the arrays, which divides the number of arrays at each step.

#Problem 2

def remove_duplicates(array):
    if not array:
        return []
    
    unique_array = [array[0]]  
    
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            unique_array.append(array[i])
    
    return unique_array

#Prove the time complexity of the algorithms

import time
import random

def remove_duplicates(array):
    if not array:
        return []
    
    unique_array = [array[0]]
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            unique_array.append(array[i])
    
    return unique_array

def remove_duplicates_in_place(array):
    if not array:
        return []
    
    write_index = 1
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            array[write_index] = array[i]
            write_index += 1
    
    return array[:write_index]

#Comment on way's you could improve your implementation

#I could've used an optimized solution for efficiency.