from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import PersonStatus, Person, PersonForm

def index(request):
	return render(request, 'portal/index.html')


def add_person(request):
    # if request.method == 'POST':
        # ...
        # return redirect('portal:index')
    personform = PersonForm()
    return render(request, 'portal/add_person.html', {'personform' : personform})


def show_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    return render(request, 'portal/person.html', {'person' : person})


def show_safe_persons(request):
    persons = None # ... change this line!
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


def search_person(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '')
    # results = Person.objects.filter(
    #     Q(first_name__icontains=text) |
    #     Q(last_name__icontains=text) |
    #     Q(other_name__icontains=text) |
    #     Q(description__icontains=text))

    # to do: render a page with the results.
