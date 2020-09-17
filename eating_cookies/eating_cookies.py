'''
Input: an integer
Returns: an integer
'''
def eating_cookies(num, cache =None):
  
  if num<0:
    return 0
  elif num ==0:
    return 1
  elif cache and cache[num]<0:
    return cache[num]
  else:
    if not cache:
      cache = {i:0 for i in range(num+1)}
    cache[num]= eating_cookies(num-1,cache)+eating_cookies(
        num-2,cache)+ eating_cookies(num-3,cache)
  return cache[num]

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

eating_cookies(5)

