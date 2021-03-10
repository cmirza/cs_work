def csWhereIsBob(names):
    # use enumerate to iterate on list and have access to index
    for count, name in enumerate(names):
        # check if name is "Bob" and return count (idx)
        if name == "Bob":
            return count
        else:
            continue
    # if "Bob" isn't found, return -1
    return -1

def csSchoolYearsAndGroups(years, groups):
    # initialize an output string
    output = ""
    # loop over the years, creating an offset to account for 0 index
    for year in range(1, years+1):
        # loop over groups, offestting by 97 (value of 'a' in chr())
        for group in range(97, 97 + groups):
            output = output + str(year) +  chr(group) + ", "
    # use slice to remove trailing comma and space
    return output[:-2]

def csMakeItJazzy(chords):
  # initialize output array
  Jazzy_List = []

  # loop over chords
  for chord in chords:
    # check if chord ends with 7
    if chord.endswith("7"):
      # add it to new list
      Jazzy_List.append(chord)
    else:
      # add it to new list and add 7
      Jazzy_List.append(chord+"7")

  return Jazzy_List

def csShortestWord(input_str):
   # initialize word list by splitting input string into an array
   word_array = input_str.split()
   # find the smallest string in the array and return the length of the string
   return len(min(word_array, key = len))

def csSumOfPositive(input_arr):
  # initalize sum int
  Positive_Sum = 0

  # loop over array of ints
  for count, value in enumerate(input_arr):
    # if value is less than 0, skip
    if value <= 0:
      continue
    # otherwise increment sum by the value
    else:
      Positive_Sum += value
  # return new sum
  return Positive_Sum

def csAnythingButFive(start, end):
  # create number list
  Number_List = list(range(start, (end+1), 1))
  # initalize list for no 5s
  No_5_List = []

  # loop over the number list
  for i, j in enumerate(Number_List):
      # if there is no 5, add it to the new list
      if '5' not in str(j):
          No_5_List.append(j)
  # return new list
  return len(No_5_List)