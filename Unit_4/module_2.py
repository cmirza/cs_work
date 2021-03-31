def csIsomorphicStrings(a, b):
    
    if len(a) != len(b):
        return False
        
    dic={}
    
    for i,x in enumerate(a):
        
        if x in dic.keys() and dic[x]!=b[i]:
            return  False
            
        elif x not in dic.keys() and b[i] in dic.values():
            return False
            
        else:
            dic[x]=b[i]
                
    return True

    def csWordPattern(pattern, a):
    
    wordList = a.split()
    
    d = {}
    s = set()
    
    if len(pattern) != len(wordList):
        return False
        
    for i in range(len(pattern)):
        if pattern[i] not in d:
            if wordList[i] in s:
                return False
            d[pattern[i]] = wordList[i]
            s.add(wordList[i])
        if d[pattern[i]] != wordList[i]:
            return False
            
    return True

from collections import defaultdict

def csGroupAnagrams(strs):

    temp = defaultdict(list)
    
    for strng in strs:
        temp[str(sorted(strng))].append(strng)
        
    res = list(temp.values())
    
    return res
    
    