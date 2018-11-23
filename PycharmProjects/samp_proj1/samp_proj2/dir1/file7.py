# task on re
import re

str = '''Email_Address,Nickname,Group_Status,Join_Year
aa@aaa.com,aa,Owner,2014
bb@bbb.com,bb,Member,2015
cc@ccc.com,cc,Member,2017
dd@ddd.com,dd,Member,2016
ee@eee.com,ee,Member,2020
'''

for i in re.finditer('([a-zA-Z]+)@([a-zA-Z]+).(com)', str): # groups starts with numbering from 1, not from 0
    print(i.group(2))

# regex is case sensitive