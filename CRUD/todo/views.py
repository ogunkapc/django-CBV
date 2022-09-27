from pyexpat import model
from django.shortcuts import render
from .models import TodoApp
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class TodoAppCreateView(CreateView):
    # specify the model for create view
    model = TodoApp
    # specify the fields to be displayed
    fields = [
        "title",
        "description"
    ]
    template_name = 'home.html'
    success_url = '/list'


class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'list.html'


class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'detail.html'


class TodoAppUpdateView(UpdateView):
    model = TodoApp
    fields = [
        "title",
        "description"
    ]
    template_name = "update.html"
    success_url = '/'


class TodoAppDeleteView(DeleteView):
    model = TodoApp
    template_name = 'delete.html'
    success_url = '/'
