'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    i = 0
    greatest = []
    while (i+k)<= len(nums):
        temp = nums[i:(k+i)]
        x = nums[i]
        for j in temp:
            
            if j>x:
                x=j
        greatest.append(x)
        i += 1
    return greatest

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

