#!/usr/bin/env python3

import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker
import random
from portal.models import Event, PersonStatus, Person


Event.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

# to do: create 30 Person objects using Faker

def generate_first_name():
	fake = Faker()
	return fake.first_name()

def generate_last_name():
	fake = Faker()
	return fake.last_name()

def generate_email():
	fake = Faker()
	return fake.ascii_safe_email()

def generate_number():
	fake = Faker()
	return fake.phone_number() 

def generate_id_number():
	fake = Faker()
	return fake.ssn(taxpayer_identification_number_type="SSN")

def generate_desc():
	fake = Faker()
	return fake.paragraph(nb_sentences=3)

def generate_other_name():
	fake = Faker()
	return fake.suffix()

def generate_status():
	statuses = PersonStatus.objects.all()
	return random.choice(statuses)


def generate_person(number):
	for i in range(0,number):
		person = Person(first_name=generate_first_name(), last_name=generate_last_name(), other_name=generate_other_name(), status=generate_status(), id_number=generate_id_number(), mobile=generate_number(), email=generate_email(), description=generate_desc())
		person.save()