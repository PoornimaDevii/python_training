# ijn25 - a single word coded with a five digit no. randomly generated which is divisible by 3
from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime


# for name in ('John','Julie','Pat'):
#     t = Template('Hello, {{name}}')
#     print(t.render(Context({'name':name})))


# t = Template('Hello {{name}}')
# for name in ('John','Julie','Pat'):
#      print(t.render(Context({'name':name})))

# person = {'name':'Sally','age':'43'}
#
# t = Template('{{person1.name}} is {{person1.age}} years old')
# c = Context({'person1':person}) # variable name is passed in the context unlike above, variable can be dict or object
# print(t.render(c))

# class Person(object):
#
#     def __init__(self,first_name,last_name):
#         self.first_nam = first_name
#         self.last_nam = last_name
#
# t = Template('Hello, {{person.first_nam.upper}} {{person.last_nam.upper}}')
# c = Context({'person': Person('Poornima','Devi')})
# print(t.render(c))
#
#person1 = Person('','')

# t = Template('{{var}} -- {{var.upper}} -- {{var.isdigit}}')
# print(t.render(Context({'var':'Hello'})))

# t = Template('Item 2 is {{items.2}}.')
# t1 = Template('Item 0 is {{items.0}}.')
# c = Context({'items':['apples','bananas','carrots']})
# print(t.render(c))
# print(t1.render(c))

# t = Template("My name is {{person.first_name}}.")
# class SilentAssertionError(AssertionError):
#
#    silent_variable_failure = True
#    class PersonClass3:
#         def first_name(self):
#             raise SilentAssertionError
#
#    p = PersonClass3()
# print(t.render(Context({'person':p})))