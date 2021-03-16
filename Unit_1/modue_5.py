def buyAndSellStock(prices):
    # if there are only two prices, just return the difference
    if len(prices) == 2:
        return prices[1] - prices[0]
    # set max_profit counter
    max_profit = 0
    # intialize current lowest price list
    current_low = [0] * len(prices)
    current_low[0] = prices[0]
    # loop over stock prices, beginning at second item in array
    for i in range(1, len(prices)):
        # if the current price is less that the last price, set a new low price
        if prices[i] < current_low[i-1]: 
            current_low[i] = prices[i]
        else:
            # otherwise set the previous low as the next low
            current_low[i] = current_low[i-1]
        # if the current price difference is greater than max profit, set as a new max profit
        if prices[i] - current_low[i-1] > max_profit:
            max_profit = prices[i] - current_low[i-1]
    return max_profit

def alphabeticShift(inputString):
    # initialize shifted string
    shifted_string = ""

    # loop over every character in input string
    for char in inputString:
        # if the character is 'z', start back over at 'a', add it to the shifted string
        if char == 'z':
            new_char = ord(char) - 25
            shifted_string += chr(new_char)
    # otherwise, increment each character by one, add it to the shifted string
        else:
            new_char = ord(char) + 1
            shifted_string += chr(new_char)
    # return the shifted string
    return shifted_string

def validParenthesesSequence(s):
    # initialize parentheses counter
    parentheses = 0
    
    # loop over characters in input string, beginning parenthesis add 1, ending parenthesis subtract 1
    for char in s:
        if char == "(":
            parentheses += 1
        elif char == ")":
            parentheses -= 1
        # if parentheses count ever drops below 0, return false
        if parentheses == -1:
            return False
    
    # if count is 0, that means you have matching parenthesis in sequence
    if parentheses == 0:
        return True
    else:
        return False
