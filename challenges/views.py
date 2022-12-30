from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
'''
def january(request):
    return HttpResponse("Finish udemy")
'''
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
    "october" : "last month of course",
    "november" : "Some projects from companies",
    "december" : "Practise and enjoy placement after 8 sem that'swhy",
}


# handling url which have number
def monthlyChallengeWithNumber(request,month):
    all_challenges_keys_list = list(all_challenges.keys())        # gettings keys like january, february
    
    # allow till 12 only as size of list is 12
    if month <= len(all_challenges_keys_list):
        month_related_to_number = all_challenges_keys_list[month-1]      # getting month name with number, used as index
        # here url is hard coded so if some changes made in url-config then it will not work 
        # so we have to extract the url using identifier    
        redirect_to = reverse("url_identifier",args=[month_related_to_number])
        return HttpResponseRedirect(redirect_to)       # redirecting to the actual url

    return HttpResponseNotFound("<h1>There are no months greater than 12</h1>")


# handling many urls 
# getting month variable from the url
def monthlyChallenge(request, month):
    try:
        challenge = all_challenges[month]
        # django can fetch file from template folder if some folder inside template folder 
        # then we have to write the path of file from template folder 
        # django uses django template language to make static html page dynamic
        # like here we send the challenge to the show_challenge.html file
        # and we can get it out in html file by {{}} . This is the syntax
        # and here { key : value} is simply a dictionary
        return render(request,
                        "challenges/show_challenge.html",   
                            {"challenge_key":challenge,"month_key":month})

    except:
        return HttpResponseNotFound("<h1>Url doesn't exist</h1>")


def index(request):
    # get all months
    all_months = list(all_challenges.keys())
    # rendering the months we create list dynamically using django template language
    return render(request,"challenges/index.html",{"months":all_months})     