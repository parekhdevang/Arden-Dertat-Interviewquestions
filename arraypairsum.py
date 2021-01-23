#Given an integer array, output all pairs that sum up to a specific value k.

def pairSum1(arr, k):
    if len(arr)<2:
        return
    arr.sort()
    left, right = (0, len(arr)-1)
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==k:
            print (arr[left], arr[right])
            left+=1 #or right-=1
        elif currentSum<k:
            left+=1
        else:
            right-=1



arr = [1,2,3,4,5,6]
k=6
pairSum1(arr,k)