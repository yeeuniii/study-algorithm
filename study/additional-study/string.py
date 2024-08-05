lst = list(range(5))

'''
Want : print <0, 1, 2, 3, 4> 
'''

# 1. print 옵션 이용
print("<", end="")
print(*lst, sep=", ", end="")
print(">")

# 2. f-string & join
sep = ", "
print(f"<{sep.join(map(str, lst))}>")

# 3. replace
print(str(lst).replace("[", "<").replace("]", ">"))