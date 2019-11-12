# Bubblesort
list_to_sort = [4,3,6,5,2]

def bubblesort(unsorted_list):
    for e in unsorted_list:
        for i in range(0,len(unsorted_list)-1):
            if unsorted_list[i]> unsorted_list[i+1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1]= temp
    return unsorted_list

print(bubblesort(list_to_sort))

