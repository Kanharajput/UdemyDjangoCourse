from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
'''
def january(request):
    return HttpResponse("Finish udemy")
'''

def monthlyChallengeWithNumber(request,month):
    if month == 1:
        return HttpResponse("1")

    else:
        return HttpResponseNotFound("Url not found")


# handling many urls 
# getting month variable from the url
def monthlyChallenge(request, month):
    challenge = None

    if month == 'january':
        challenge = "Finish udemy course"

    elif month == 'february':
        challenge = "Socha nahi"

    elif month == 'march':
        challenge = "Attend marriages"

    else:
        return HttpResponseNotFound("Url not found")
        
    return HttpResponse(challenge)