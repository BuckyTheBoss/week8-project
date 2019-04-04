from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
	path('person/<int:person_id>', views.show_person, name='person'),
	path('person/add', views.add_person, name='add_person'),
	path('person/show_safe', views.show_safe, name='show_safe'),
	path('person/search', views.search_person, name='search_person'),
	path('person/edit/<int:person_id>', views.edit_person, name='edit_person')

    # to do: add more paths...
]