from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-consent', views.getConsent, name='get-consent')
]