from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Event(models.Model):
    CATEGORY = (
        ('fire', 'Fire'),
        ('earth', 'Earth'),
        ('water', 'Water'),
        ('storm', 'Storm'),
        ('disease', 'Disease'),
        ('industrial', 'Industrial')
    )

    SEVERITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None, blank=True)
    location = models.CharField(max_length=200)
    severity = models.CharField(max_length=10, choices=SEVERITY,
                                default='medium')
    category = models.CharField(max_length=10, choices=CATEGORY,
                                default='fire')

    def __str__(self):
        return "{} [{}] at {}".format(
            self.name, self.severity, self.location)


class PersonStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# to do: add Person model
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=11)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    description = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(PersonStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {} {}".format(
            self.id, self.first_name, self.last_name)


class PersonForm(ModelForm):    
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'other_name', 'id_number', 'mobile', 'email', 'description','status']

