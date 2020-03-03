from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Info, Book, GeeksModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookCreateForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class InfoList(LoginRequiredMixin, ListView, View):
    model = Info
    context_object_name = 'azamat'
    # raise_exceptionq = True
    login_url = '/register/'


class BookCreateView(CreateView):
    template_name = 'blog/info_list.html'
    form_class = BookCreateForm
    success_url = '/login/'


class InfoList2(LoginRequiredMixin, ListView, View):
    model = Book
    context_object_name = 'con'
    login_url = '/register/'


# ------------------
class GeeksCreate(CreateView):
    # specify the model for create view
    model = GeeksModel

    # specify the fields to be displayed
    fields = ['title', 'description']
    success_url = '/show_some/'


class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel


class GeeksDetailView(DetailView):
    # specify the model to use
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    # specify the model you want to use
    model = GeeksModel

    # specify the fields
    fields = [
        "title",
        "description"
    ]

    # can specify success url
    # url to redirect after sucessfully
    # updating details
    success_url = "/"


class GeeksDeleteView(DeleteView):
    model = GeeksModel

    # can specify success url
    # url to redirect after sucessfully
    # deleting object
    success_url = "/"
