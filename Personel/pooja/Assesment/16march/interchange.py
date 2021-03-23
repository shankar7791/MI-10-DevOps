def swaplist(List):
    size = len(List)
    temp = List[0]
    List[0] = List[- 1]
    List[-1] = temp
    return List


List = ['p', 'o', 'o', 'j', 'a']
print(swaplist(List))
