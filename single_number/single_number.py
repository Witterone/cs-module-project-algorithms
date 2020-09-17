'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    temp = set()
   
    for i in arr:
        if i in temp:
            temp.remove(i)
        else:
            temp.add(i)
    
    
    return temp.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    
    