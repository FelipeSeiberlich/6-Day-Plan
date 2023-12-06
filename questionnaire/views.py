from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome_questionnaire(request):
    return HttpResponse("Welcome to the 6 DAY-PLAN Questionnaire.")
