#make an array for the sorting of this selection
array = [24, 23, 26, 27, 29, 14, 16]
#functional header for the selection sort, and we're calling for the array
def selectionsort(array)
    #variable for the length of the array
    n = len(array)
#whatever the length of the array is how many times you'll iterate the for loop
    for i in range(n)

    #initially assume the first element of the unsorted part as the minimum
#creating the minimum value as i
        minimum = i
        #for loop
        for j in range(i+1, n):

            if (array[j] < array[minimum]): #comparison operator that is nested
            #Update position of minimum element if a smaller element is found.
            minimum = j

        #swap the minimum element with the first element of the unsorted part
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array
#printing the selection sort array
print(selectionSort(array))