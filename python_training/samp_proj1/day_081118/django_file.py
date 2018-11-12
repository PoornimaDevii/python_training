# To check the status of apache2 - service apache2 status
# to create a django project - django-admin.py startproject mysite
# django-admin.py startproject mysite
# (venv) cisco@cisco-ThinkPad-T430:~/PycharmProjects/samp_proj1$ cd mysite
# (venv) cisco@cisco-ThinkPad-T430:~/PycharmProjects/samp_proj1/mysite$ python manage.py runserver

import django

# Django is a MTV framework (model template view) and not MVCp, cause controller ( which takes the input) is not there (cause
# django doesn't take input but only provides large output

# ^C(venv) cisco@cisco-ThinkPad-T430:~/PycharmProjects/samp_proj1/mysite$ python manage.py shell
# Python 3.5.1+ (default, Mar 30 2016, 22:46:26)
# [GCC 5.3.1 20160330] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from django.template import Template
# >>> t = Template("My name is {{name}}.")
# >>> print(t)
# <django.template.base.Template object at 0x7f45473bd7f0>
# >>> from django.template import Context
# >>> c = Context({"name":
# ... "Poornima"})
# >>> t.render(c)
# 'My name is Poornima.'
# >>>print(t.render(c))
# My name is Poornima.
from django.template import Template,Context

# Bad way
# for name in ('John','Julie','Pat'):
#     t = Template('Hello, {{name}}')
#     print(t.render(Context({'name':name})))

# Good way

# t = Template('Hello {{name}}')
# for name in ('John','Julie','Pat'):
#     print(t.render(Context({'name':name})))

# python3 manage.py shell < filename.py ( to run from python file)3 ( after keeping the file to be executed where
# manage.py exists


