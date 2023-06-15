'''
Merge sort is similar to the quick sort algorithm as it uses the divide and conquer approach to sort the elements.
It divides the given list into two equal halves, calls itself for the two halves and then merges the two sorted halves.
There are a bunch of sorting algorithms in computer science such as Bubble sort, Selection sort, Insertion Sort, quick sort and Merge sort.
All these algorithms do the same work but with a different approach.
The merge sort algorithm is currently the most efficient approach to sort the elements of an array.

'''

def merge(listA, listB):
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        newlist = merge(left, right)
        return newlist

a = [56, 89, 45, 34, 90, 32, 20, 67, 43]
print(merge_sort(a))
