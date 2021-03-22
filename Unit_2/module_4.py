def fibonacciSimpleSum2(n):
    def fib(n):
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        else:
            fibs = fib(n-1)
            fibs.append(fibs[-1] + fibs[-2])
            return fibs
    d = {}
    
    for i in range(len(fib(50))):
        array = fib(50)
        check =  n - array[i]
        if array[i] in d:
            return True
        else:
            d[check] = i
            
    return False 


def csBinarySearch(nums, target):
    
    min_idx = 0
    max_idx = len(nums) -1
    
    while min_idx <= max_idx:

        mid_idx = (min_idx + max_idx) // 2
        
        if nums[mid_idx] == target:
            return mid_idx
        
        elif nums[mid_idx] < target:
            min_idx = mid_idx + 1
            
        else:
            max_idx = mid_idx -1
            
    return - 1


    