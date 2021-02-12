def csReverseString(chars):
  # initalize counter for first (beginning) pointer
  point_1 = 0
  # initialize counter for second (end) pointer
  point_2 = len(chars)-1
  # run while loop until start and end collide
  while point_1 < point_2:
    # swap chars
    chars[point_1],chars[point_2] = chars[point_2],chars[point_1]
    # increment first pointer
    point_1+=1
    # increment second pointer
    point_2-=1
  # return revrsed array
  return chars

  def csCheckPalindrome(input_str):
  # initalize counter for first (beginning) pointer
  point_1 = 0
  # initialize counter for second (end) pointer
  point_2 = len(input_str)-1
  # run while loop until start and end collide
  while point_1 < point_2:
    # check if chars match, if they do, continue
    if input_str[point_1] == input_str[point_2]:
      point_1+=1
      point_2-=1
      continue
    # if they don't, return false
    else:
      return False
  # if loop completes, return true
  return True

def csRemoveDuplicateWords(input_str):
  # turn input string into an list
  input_arr = input_str.split()
  # initialize de-duplicated list
  dedeup_arr = []

  # use list comprehension to only add unique items to dedupe list
  [dedeup_arr.append(word) for word in input_arr if word not in dedeup_arr] 

  # join list items with a space and return
  return (' '.join(dedeup_arr))