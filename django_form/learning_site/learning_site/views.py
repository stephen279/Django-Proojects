from django.shortcuts import render

from . import forms


def hello_world(request):
    return render(request, 'home.html')

def suggestion_view(request):
    form = forms.suggestionForm() #instanciate from
    if request.method == "post":
        form = forms.SuggestionForm(request.POST)  #all form data come in and put into form
        if form.is_valid():
            print("good form")
    return render(request, 'suggestion_form.html', {'form':form})  #send instanciated form out t the templete