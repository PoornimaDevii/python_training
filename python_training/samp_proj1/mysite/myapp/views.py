from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
import datetime


# Create your views here. when post is used, data is packed in a file and sent, but in get, data is got using command line arguments
# cookies are served on client, sessions on server side
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Publisher
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm




def say_hello(request,name):
    if name == 'san':
        return HttpResponse("Hello World",name)
    else:
        return HttpResponse("Hi",name)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s" %now
    return HttpResponse(html)

def hours_ahead(request,offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours, it will be %s" %(offset, dt)
    return HttpResponse(html)

def current_datetime1(request):
    now = datetime.datetime.now()
    return render_to_response('html1.html',{'now1':now})

def create_form(request):
    return render_to_response('html3.html',{})

# use the below instead of above
# def search_func(request):
#     return render(request,'html2.html')

# def search(request):
#     if 'q' in request.GET and 'q' != '':
#         print('=====',request.GET)
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form'
#     return HttpResponse(message)

@csrf_exempt
def search(request):
    if 'p_city' in request.POST:
        req = request.POST['p_city']
        pub_name = Publisher.objects.filter(city=req)
        #print(pub_name)
        return render_to_response('html3.html',{'data': pub_name})
    else:
        return HttpResponse('You have submitted an invalid response')


class ArticleForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name','address','city','state_province','country','website']

form = ArticleForm()
print(form)


# def render_made_form(request):
#     return render_to_response('html4.html',{})
# from .myblog.forms import PostForm
# def post_new1(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

def get_color(request):
    return render_to_response('my_cookie.html',{})

def set_color(request):
    if 'favorite_color' in request.GET:
        response = HttpResponse("Your favourite color is now %s" % request.GET['favorite_color'])
        response.set_cookie('favorite_color', request.GET['favorite_color'])
        return response
    else:
        return HttpResponse("You didn't give a favorite color")

def show_color(request):
    if 'favorite_color' in request.COOKIES:
        return HttpResponse("Your favourite color is %s" % request.COOKIES['favorite_color'])

    else:
        return HttpResponse("You don't have a favourite color")

#
# def login(request):
#     if request.method == 'POST':
#         if request.session.test_cookie_worked():
#             request.session.delete_test_cookie()
#             return HttpResponse("You're logged in")

def login_page(request):
    return render_to_response('username.html',{})


def login_as_user(request):
    with open('/home/cisco/PycharmProjects/samp_proj1/mysite/myapp/username.txt') as file:
        f = file.readline()
        a = f.split(':')
        b = list(map(lambda x: x.strip('\n'),a))
    if b[0]==request.GET['username'] and b[1]==request.GET['password']:
            response1 = HttpResponse("You are logged in as %s" % request.GET['username'])
            response1.set_cookie('username', request.GET['username'])
            response1.set_cookie('password',request.GET['password'])
            #if 'username' in request.COOKIES and 'password' in request.COOKIES:
            print("logged in successfully")
            return render(request,'html2.html')
            #return HttpResponse("You're successfully logged in with username as %s, and password as %s!" \
             #                   %(request.GET['username'],request.GET['password']))
    else:
        return HttpResponse("Not correctly logged in")

def search_call(request):
    return render_to_response('search_pg.html',{})

# if cookie not set and someone entering from search page
def return_to_search(request):
    if 'username' in request.COOKIES:
        return redirect('/form/')


#def user_logout(request):







