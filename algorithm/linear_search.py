def linear_search(list,target):
    
    for i in range(0,len(list)):
        if(list[i]==target):
            return i
    return None

def verify(index):
    if index is not None:
        print("Data Found at index", index)
    else:
        print("Data Not Found")

numbers=[1,2,3,4,5,6,7,8]
result=linear_search(numbers,3)
verify(result)