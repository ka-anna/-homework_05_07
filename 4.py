#Implement binary search algorithm iterative

def bins (x, ls):
    if x in ls[0:len(ls)//2]:
            print(ls.index(x))
    elif x in ls [len(ls)//2:]:
            print(ls.index(x))
    else:
            print("Missing value")   
bins(x=4,ls = [1,5,3,4,6])
