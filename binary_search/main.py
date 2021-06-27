# find the number

lst = [1,3,4,5,6,545]
answer = 545
sorted_lst = sorted(lst)

print(sorted_lst)

def find_bin(arr,x):
    mid = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high+low)//2
        
        if arr[mid] < answer:
            low = mid+1
        elif arr[mid] > answer:
            high = mid-1
        else:
            return mid
    return -1
            
print(find_bin(lst,answer))