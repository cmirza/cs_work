def condense_linked_list(node):
    
    previous = node
    current = previous.next
    keys = [previous.value]

    while current:
        
        currentVal = current.value

        if currentVal in keys:
            previous.next = current.next
            current = current.next

        else:
            keys.append(currentVal)
            previous = current
            current = previous.next

    return node


def first_not_repeating_character(s):
    
    table = {}
    
    for i in range(len(s)):
        if s[i] not in table:
            table[s[i]] = 1
        else:
            table[s[i]] += 1
    
    for k, v in table.items():
        if v == 1:
            return k
            
    return '_'

def uncover_spy(n, trust):

    cache = {}
    trusted = {}
    spys = []

    for p in range(1, n + 1):
        cache[p] = []
        trusted[p] = 0

    for pair in trust:
        cache[pair[0]].append(pair[1])
        trusted[pair[1]] += 1

    for p in cache:
        if len(cache[p]) == 0 and trusted[p] == (n - 1):
            spys.append(p)
        
    return -1