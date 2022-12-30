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
        return render(request,"challenges/show_challenge.html")

    except:
        return HttpResponseNotFound("<h1>Url doesn't exist</h1>")


def index(request):
    link_of_month = ""
    months = list(all_challenges.keys())           # getting months name

    for month in months:
        month_capitilize = month.capitalize()
        url_of_month = reverse("url_identifier",args=[month])
        link_of_month += f"<li><a href=\"{url_of_month}\">{month_capitilize}</a></li>"

    response = f"<ul>{link_of_month}</ul>"
    return HttpResponse(response)