'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    temp = []
    cnt = 0
    
    for i in arr:
        if abs(i) > 0:
            temp.insert(cnt,i)
            cnt+=1
        else:
            temp.append(i)
            
    return temp           

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    
