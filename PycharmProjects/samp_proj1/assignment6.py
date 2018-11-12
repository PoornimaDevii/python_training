# Transpose a list of lists

l = [int(x) for x in input().split(',')]
ll = [l.append(list(x)) for x in input()]
print(ll)

