from django.shortcuts import render
from .models import Person
# Create your views here.
def home(request):
    people = Person.objects.all()
    return render(request,'home.html',{'people':people})
