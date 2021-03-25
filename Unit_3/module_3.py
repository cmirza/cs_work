def csFindAllPathsFromAToB(graph):
    
    list = []
    
    def findpath(n = 0, root = [0]):
        if n < len(graph)-1:
            for i in graph[n]:
                findpath(i, root+[i])
        else:
            list.append(root)
            
    findpath()
    
    return list