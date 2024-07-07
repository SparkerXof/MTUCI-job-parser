from django.shortcuts import render
from django.http import HttpResponseRedirect

from parser.forms import VacationForm
from parser.parsing import process_vacation_form

def index(request):
    return HttpResponseRedirect("/vacations/")

def vacations(request):
    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            process_vacation_form(form)
            return HttpResponseRedirect("/vacations/")
    else:
        form = VacationForm()
    context = {"form": form, "type": "/vacations/"}
    return render(request, "parser/index.html", context)
