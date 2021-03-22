def reverseLinkedList(l):
    # set pointers for previous and current nodes
    prev = None
    curr = l
    
    # walk through list    
    while curr:
        # change current next to temp
        temp = curr.next
        # swap current and previous values
        curr.next = prev
        prev = curr
        # set temp to current so the loop knows where to go next
        curr = temp
    # return previous which will be the new head reference
    return prev


# using counter method to make life easier
from collections import Counter

# using counter method to make life easier
from collections import Counter

def checkBlanagrams(word1, word2):

    # get the number of characters for each input word
    charCount1 = Counter(word1)
    charCount2 = Counter(word2)
    
    # subtract the number of characters of the first word from the second word, if count is equal to 1 char difference, return true
    return sum((charCount1 - charCount2).values()) == 1



def findValueSortedShiftedArray(nums, target):
    
    min_idx = 0
    max_idx = len(nums)-1
	
    while min_idx <= max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if target == nums[mid_idx]:
            return mid_idx
        if nums[min_idx] <= nums[mid_idx]:
            if target > nums[mid_idx] or target < nums[min_idx]:
                min_idx = mid_idx + 1
            else:
                max_idx = mid_idx - 1
        else:
            if target < nums[mid_idx] or target > nums[max_idx]:
                max_idx = mid_idx - 1
            else:
                min_idx = mid_idx + 1
    return -1