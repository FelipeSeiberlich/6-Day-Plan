from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_questionnaire_questions(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'questionnaire/questionnaire_questions.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_questionnaire_questions')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'questionnaire/add_item.html', context)

def edit_item(request, item_id):
    return render(request, 'questionnaire/edit_answer.html')

