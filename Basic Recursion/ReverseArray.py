def reverseArray(list,left,right):
    if left >= right :
        return
    list[left],list[right] = list[right],list[left]

    return reverseArray(list,left+1,right-1)

list=[1,2,3,4,5]
reverseArray(list,0,len(list)-1)
print(list)