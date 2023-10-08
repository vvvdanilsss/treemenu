from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    path('about/history/', views.history, name='history'),
    path('about/mission/', views.mission, name='mission'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
]
