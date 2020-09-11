from django.shortcuts import render
from .models import Points, Groops

# Create your views here.
def index(request, lan_r):
	context = {
		'points': Points.objects.all(),
		'groops': Groops.objects.all(),
		'add_point': set_session()
	}
	return render(request, 'maps/index.html', context)

def set_session(request, point_id):
	request.session['your_points'] += point_id