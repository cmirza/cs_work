def csLongestPossible(str_1, str_2):
    # initialize array for longest characters
    unique_chars = []

    for i in str_1:
        # check if character is in unique_chars array
        if i not in unique_chars:
            # add to unique_chars
            unique_chars.append(i)
    
    for j in str_2:
        # check if character is in unique_chars array
        if j not in unique_chars:
            # add to unique_chars
            unique_chars.append(j)
    
    # sort the unique characters
    unique_chars.sort()
    
    # turn the array into a string and return it
    return ''.join(unique_chars)

# probably O(n^2) due to nested loop
def csSortedTwoSum(numbers, target):
    # loop over the array while maintaining their index
    for i, num1 in enumerate(numbers):
        # then loop over the array again, offset by one
        for num2 in numbers[i+1:]:
            # if the sum of the number from the first loop and second loop equals the target
            if num1 + num2 == target:
                # return the index of the two numbers
                return numbers.index(num1), numbers.index(num2)

def csFirstUniqueChar(input_str):

    # initalize a list for character indicies
    chars_index = []

    # loop over characters in input string
    for char in range(len(input_str)):
      # use list comprehension to check the number of occurances for each character
      chars_index.append(len([i for i in input_str if i == input_str[char]]))
    # if any character occurs only once, return that index
    if 1 in chars_index:
      return chars_index.index(1)
    # otherwise return -1
    else: 
      return -1