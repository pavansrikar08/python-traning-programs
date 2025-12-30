def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(len_half) and j < len(right_half[j]):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i +=1
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1 
        while i < len(left_half):
            arr[k] = left_half[i]
            print(arr)
            i+=1 
            k+=1 
        while j < len(right_half):
            arr[k] = right_half[j]
            print(arr)
            j+=1
            k+=1 
arr = list(map(int, input().split()))
merge_sort(arr)
print("sorted array:",arr)
    