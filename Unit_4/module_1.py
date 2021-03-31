from collections import Counter

def csFindTheSingleNumber(nums):

    freq = Counter(nums)
     
    for i in freq:
       
        if(freq[i] == 1):
            return i


def csAverageOfTopFive(scores):
    d = {}
    out = []
    for i in scores:
        if i[0] not in d:
            d[i[0]] = []
        d[i[0]].append(i[1])
    for e in d:
        d[e].sort()
        sortScores = d[e][-5:]
        out.append([e, sum(sortScores) // len(sortScores)])
    return out


def csMaxNumberOfLambdas(text):

    lambda_letters = {"l": 0, "a": 0, "m": 0, "b": 0, "d": 0}
    
    for char in text:
        if char in lambda_letters:
            lambda_letters[char] += 1
    
    
    return min(lambda_letters.values())