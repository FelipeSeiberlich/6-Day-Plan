from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_questionnaire_questions(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'questionnaire/questionnaire_questions.html', context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('user_answer')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_questionnaire_questions')
    return render(request, 'questionnaire/add_item.html')

