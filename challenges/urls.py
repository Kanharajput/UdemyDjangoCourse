from django.urls import path
from . import views

""" month can be anythink jan, feb, march....
    it is know as dynamic path
    here month is an identifier """
    # set name to the path for which we are generating url using reverse method
urlpatterns = [  # here sequence matters so int url should be above str otherwise it will not work
    path('<int:month>', views.monthlyChallengeWithNumber),          # this will handle integer values url like 1 or 2 ....
    path('<str:month>', views.monthlyChallenge, name="url_identifier"),         # this will handle only string urls
    #path('january', views.january)
    path("",views.index),
]