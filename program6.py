def Sum(List, size, sum):
    sumList = []
    if size == 1:
       for x in List:
           sumList.append(sum + x)
       return sumList
    l2 = list(List)
    for x in List:
       l2.remove(x)
       sumList.extend(Sum(l2, size-1, sum + x))
       return sumList

def summation(List, size):
    sumList = list(List)
    for i in range(2, size + 1):
        sumList.extend(Sum(List, i, 0))
        number = 1
        while True:
            if number not in sumList:
                print("The least integer which is not present in the list and also can't be represented as the summation of sum-element is",number)
                break
            number += 1
size = int(input("Enter the no. of elements you want to add in the list : "))
List = []
print("Enter the elements of list : ")
for i in range(size):
    List.append(int(input()))
summation(List, size)







