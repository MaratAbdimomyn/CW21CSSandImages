from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *

class OneView(ListView):
    model = Phone
    template_name = 'index.html'
    context_object_name = 'ones'

class AboutView(DetailView):
    model = Phone
    template_name = 'about.html'
    context_object_name = 'one'

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        filter = Phone.objects.filter(brand = search)
        context = {'filter':filter}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

def add_image(request):
    data = Images.objects.all()
    if request.method == 'POST':
        img = Images.objects.create(image = request.FILES['image'])
        img.save()
        return render (request, 'create_image.html', {'data':data})
    else:
        return render (request, 'create_image.html', {'data':data})