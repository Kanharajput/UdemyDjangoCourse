from django.urls import path
from . import views

""" month can be anythink jan, feb, march....
    it is know as dynamic path
    here month is an identifier """
urlpatterns = [
    path('<month>', views.monthlyChallenge),
    #path('january', views.january)
]