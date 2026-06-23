from typing import List
def count_freq(nums:List[int])->dict:
    dict={}
    for i in nums:
        dict[i]=dict.get(i,0)+1
    
    return dict

list=[1,2,2,3,1]
k=count_freq(list)
print(k)