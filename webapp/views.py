from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


def index(request):
    return render(request, 'index.html', {})

'''class IndexView(ListView):
    template_name = 'index.html'
    '''
