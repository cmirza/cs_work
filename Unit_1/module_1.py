def csAlphanumericRestriction(input_str):
    # check if input is all digits
    if input_str.isdigit():
        return True
    # check if input is all letters
    if input_str.isalpha():
        return True
    # otherwise return false
    else:
        return False

def csOppositeReverse(txt):
    # use slicing method to reverse string and swapcase function to switch casing
    return txt[::-1].swapcase()

def csSquareAllDigits(n):
    #convert int to str, so we can iterate over chars
    nums = list(str(n))
    #square each number and add it to a new array
    new_nums = [int(x)**2 for x in nums]
    #join arr into a new str
    output_nums = ''.join(str(y) for y in new_nums)
    #return str as an int
    return int(output_nums)

def csRemoveTheVowels(input_str):
    # kinda brute force, but works
    input_str = input_str.replace("a","")
    input_str = input_str.replace("e","")
    input_str = input_str.replace("i","")
    input_str = input_str.replace("o","")
    input_str = input_str.replace("u","")
    input_str = input_str.replace("A","")
    input_str = input_str.replace("E","")
    input_str = input_str.replace("I","")
    input_str = input_str.replace("O","")
    input_str = input_str.replace("U","")
    return input_str
