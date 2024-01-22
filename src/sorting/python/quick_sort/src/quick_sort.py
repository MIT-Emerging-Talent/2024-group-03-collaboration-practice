def quicksort_v1(list1):

    def quicksort(list1, left, right):
        if left<right:
            split = partition(list1, left, right)
            quicksort(list1, left, split-1)
            quicksort(list1, split+1, right)


    def partition(list1, left, right):
        pivot = list1[right]
        i = left
        j = right-1

        while i<j:

            while list1[i] < pivot and i < right:
                i += 1
            while list1[j] >= pivot and j > left:
                j -= 1
            
            if i<j:
                list1[i], list1[j] = list1[j], list1[i]
        
        if list1[i] > pivot:
            list1[i], list1[right] = list1[right], list1[i]

        return i
    
    left = 0
    right = len(list1)-1
    quicksort(list1, left, right)
    return list1



def quicksort_v2(list1):

    def quicksort(list1, left, right):
        '''Take a list, '''
        if left<right:
            split = partition(list1, left, right)
            quicksort(list1, left, split-1)
            quicksort(list1, split+1, right)

    def partition(list1, left, right):
        pivot = list1[right]
        i = left
        j = right-1

        while i<j:

            while list1[i] < pivot and i < right:
                i += 1
            while list1[j] >= pivot and j > left:
                j -= 1
            
            if i<j:
                list1[i], list1[j] = list1[j], list1[i]
        
        if list1[i] > pivot:
            list1[i], list1[right] = list1[right], list1[i]

        return i
    
    left = 0
    right = len(list1)-1
    quicksort(list1, left, right)
    return list1
# print(quicksort_v1([2, 5, 1, 4, 3]))
