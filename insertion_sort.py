# Insertion sort function
unsorted_list= [3,4,2,1]

def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        current_val = unsorted_list[i]
        k = i-1
        while( k>=0) and current_val< unsorted_list[k]:
                unsorted_list[k+1] = unsorted_list[k]
                k -=1
        unsorted_list[k + 1] = current_val
    return unsorted_list

print(insertion_sort(unsorted_list))

