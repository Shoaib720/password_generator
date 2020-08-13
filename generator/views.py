from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'asdhf4398fayf'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specialChar'):
        characters.extend(list('!@#$%&'))

    password = ''

    for i in range(length):
        password += random.choice(characters)
    return render(request, 'generator/password.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')
