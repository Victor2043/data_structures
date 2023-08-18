#class Solution:
 #   def __init__(self):
  #      pass

def fixed_sliding_window(nums: list[int], window_size: int) -> list[list[int]]:
    i = 0
    result = []
    while i < len(nums):
        if len(nums[i:window_size+i]) != window_size:   
            break
        
        if(window_size > 1):
            result.append(nums[i:window_size+i])
        else:
            result.append([nums[i]])
        
        i += 1
    
    return result

def sw():
    return True