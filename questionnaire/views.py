from django.shortcuts import render

# Create your views here.
def get_questionnaire_questions(request):
    return render(request, 'questionnaire/questionnaire_questions.html')
