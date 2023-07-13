#Implement search algorithm iterative

def search(ls, target):
    for i in range(len(ls)):
      if ls[i]==target:
        return i
    return "target isn't in ls"
print(search(ls = [1,2,4,5], target = 4))
