from django.shortcuts import render
from mainpage.locale import Links
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .models import Chronology

# Create your views here.
def chronology(request, lan_r):
    try:
        return render(request, 'chronology/chronology.html', {'chronology': Links.chronology[lan_r], 'chronology_el': Chronology.objects.order_by('-date')})
    except:
        return HttpResponseNotFound()
        # return redirect('../../en/')