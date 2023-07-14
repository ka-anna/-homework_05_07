#Implement the insertion sort algorithm to sort a given list of elements in ascending order. insertion_sort(array: list) -> list


def insertion_sort(array):
   
      for i in range (1, len(array)):  
         k = i
         while k >0:
            if array[k] < array[k-1]:
               array[k], array[k-1] = array[k-1], array[k]
            k-=1

      return array
print(insertion_sort([1,3,2,7,6,8,4,9]))
