def csFriendCircles(friendships):
    visited = []
    stack = []
    count = 0
    for i in range(len(friendships)):
        if i not in visited:
            count += 1
            stack.append(i)
        while stack:
            node = stack.pop()
            visited.append(node)
            for j, friend in enumerate(friendships[node]):
                if friend == 1 and j not in visited:
                    stack.append(j)
    return count