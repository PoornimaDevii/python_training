import re

pattern1 = 'hello' # pattern1 = 'hello' is also acceptable, but adding metacharacters re.compile usage
# is mandatory
text = 'hello, is this pattern found hello?'

match1 = re.search(pattern1, text)

print(1,match1)
print(2,type(match1))

print(3,match1.re.pattern)
print(4,match1.start())
print(5,match1.end())

# for match in re.findall(pattern1,text): # returns the string as such when it is repeated
#     print(match)
#
# for match_it in re.finditer(pattern1,text): # returns the location of the repeated string(pattern)
#     print(match_it)
#     print(match_it.start())
#     print(match_it.end())
#     print(match_it.re.pattern)

