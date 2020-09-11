from django.shortcuts import render
# from django.contrib.auth import logout
from django.shortcuts import redirect
from .locale import lan
from django.http import HttpResponseNotFound
from .locale import Links, lanlist
from maps.models import Points

def error_lan(lan_r):
    if lan_r in lanlist:
        return False
    else:
        return True

# def get_lan(lan_r, page):
#     eval('return Links.'+ str(page) +'["'+ lan_r +'"]')

# Create your views here.
def lang(request):
    if request.session.get('lan'):
        return redirect(request.session.get('lan')+'/')
    else:
        return redirect(lan+'/')


def index(request, lan_r):

    request.session['lan'] = lan_r

    print(request.session.get('lan')[0])

    request.session['lan'] = lan_r
    # redirect('/ru').set_cookie('lan', str(lan_r))

    language = request.session.get('lan')

    if error_lan == True:
        return HttpResponseNotFound()
    else:
        return render(request, 'mainpage/index.html', {'links': Links.mainpage[lan_r], 'languages': lanlist})


def documentation(request, lan_r):
    if error_lan == True:
        return HttpResponseNotFound()
    else:
	    return render(request, 'mainpage/documentation.html')


def about(request, lan_r):
    if error_lan == True:
        return HttpResponseNotFound()
    else:
	    return render(request, 'mainpage/about.html', {'links': Links.about[lan_r]})


def contacts(request, lan_r):
    if error_lan == True:
        return HttpResponseNotFound()
    else:
	    return render(request, 'mainpage/contacts.html')


def start(request, lan_r):
    if error_lan == True:
        return HttpResponseNotFound()
    else:
        context = {
		    'points': Points.objects.all(),
            'links': Links.start_page[lan_r]
	            }
        return render(request, 'maps/index.html', context)