from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
	path('person/<int:person_id>', views.show_person, name='person'),
	path('person/add', views.add_person, name='add_person')
    # to do: add more paths...
]