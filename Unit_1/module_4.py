def csReverseIntegerBits(n):
  # convert input into bin, turn it into a string and slice off 2 leading characters
  binary_n = str(bin(n))[2:]

  # reverse the binary string and convert it into an int
  binary_reverse = int(binary_n[::-1], 2)

  # return result
  return binary_reverse

def csBinaryToASCII(binary):

  # intialize an array for operating on binary string
  binary_array = []

  # loop over the array by every 8 chars
  for index in range(0, len(binary), 8):
    #capture the next 8 characters, covert into binary, then integer then ASCII
    converted_chr = chr(int(binary[index : index + 8], 2))
    #add the converted char to the array
    binary_array.append(converted_chr)
  
  # return the array converted to a string
  return ''.join(binary_array)

def csRaindrops(number):

  # initialize return string
  return_str = ""

  # if 3 is a factor, add Pling
  if number % 3 == 0:
    return_str += "Pling"
  # if 5 is a factor, add Plang
  if number % 5 == 0:
    return_str += "Plang"
  # if 7 is a factor, add Plong
  if number % 7 == 0:
    return_str += "Plong"
  
  # if string is empty, return the number as a string
  if return_str == "":
    return str(number)
  # otherwise, return the string
  else:
    return return_str
