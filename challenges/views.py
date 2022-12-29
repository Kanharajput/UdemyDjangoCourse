from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
'''
def january(request):
    return HttpResponse("Finish udemy")
'''
# handling url which have number
def monthlyChallengeWithNumber(request,month):
    if month == 1:
        return HttpResponse("1")

    else:
        return HttpResponseNotFound("Url not found")

# all month challenges it like an switch statement as python doesn't have switch
# it prevent us from typing different if condition for all months
all_challenges = {
    "january" : "Finish udemy course",
    "february" : "Socha nahi",
    "march" : "Attend marriages",
    "april" : "Exam prepration",
    "may" : "Write exam",
    "june" : "Enroll a course",
    "july" : "Practise of course",
    "august" : "course take 5 months and it is 3rd",
    "september" : "complete previous learnt things",
    "octomber" : "last month of course",
    "novermber" : "Some projects from companies",
    "december" : "Practise and enjoy placement after 8 sem that'swhy",
}

# handling many urls 
# getting month variable from the url
def monthlyChallenge(request, month):
    try:
        challenge = all_challenges[month]
        print(challenge)
        return HttpResponse(challenge)

    except:
        return HttpResponseNotFound("Url doesn't exist")