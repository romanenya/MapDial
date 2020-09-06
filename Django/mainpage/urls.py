from django.urls import path
from django.conf.urls import include
from . import views
from .locale import lan, lanlist
from chronology.views import chronology

urlpatterns = [
    path('', views.lang),
    path('<str:lan_r>/', views.index),
    path('<str:lan_r>/documentation', views.documentation),
    path('<str:lan_r>/about', views.about),
    path('<str:lan_r>/contacts', views.contacts),
    path('<str:lan_r>/start', views.start),
    path('<str:lan_r>/chronology', chronology)
]
