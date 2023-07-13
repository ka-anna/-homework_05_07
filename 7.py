#Implement the bubble sort algorithm to sort a given list of elements in ascending order . bubble_sort(array: list) -> list 


def bubble_sort(array):
      k = 1
      while len(array)-k>1:
       for i in range(len(array)-k):
            if array[i]> array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
       k+=1 
      return array
print(bubble_sort([1,3,4,5,2]))
