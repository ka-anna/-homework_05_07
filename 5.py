#Implement an iterative binary search algorithm that searches for a target element within a sorted array.

def bin_s(ls,target):
    end =len(ls)-1
    start = 0
    ls.sort()
    while start <= end:
        index_m = (start + end)//2
        if target == ls[index_m]:
            return index_m
        elif target > ls[index_m]:
             start = index_m + 1
        else: 
             end = index_m - 1
    return "Error"
        
print(bin_s([1,3,2,4,5,6,8,7],11))
