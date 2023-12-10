from django.shortcuts import render
from .models import Item

# Create your views here.


def get_questionnaire_questions(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'questionnaire/questionnaire_questions.html', context)

def add_item(request):
    return render(request, 'questionnaire/add_item.html')

