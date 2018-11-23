import re


# Andy 	0
# Mandi 	10
# Sandy 	20
# Hollie 	18
# Molly 	19
# Dollie 	15


#pattern = '(i$|ie$)(,)'
str = 'andy,mandi,sandy,hollie,molly,dollie,'
temp = []
for i in re.finditer('(i$|ie$)(,)', str):
    print(i.group(1))
    temp.append(i.group(1))

print(temp)

# Andy 	0
# Mandi 	10
# Sandy 	20
# Hollie 	18
# Molly 	19
# Dollie 	15


pattern = re.compile('([a-zA-z]+)([dy]|[di]|[lie]|[ly]$)')
temp = []
for i in re.finditer(pattern, str):
    temp.append(i.group(1))

print(temp)