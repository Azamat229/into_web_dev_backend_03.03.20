from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Info, Book, GeeksModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookCreateForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


class InfoList(LoginRequiredMixin, ListView, View):
    model = Info
    context_object_name = 'azamat'
    # raise_exceptionq = True
    # login_url = '/register/'


class BookCreateView(CreateView):
    template_name = 'blog/info_list.html'
    form_class = BookCreateForm
    success_url = '/login/'


class InfoList2(LoginRequiredMixin, ListView, View):
    model = Book
    context_object_name = 'con'
    # login_url = '/register/'


# ------------------
class GeeksCreate(CreateView):
    model = GeeksModel

    fields = ['title', 'description']
    success_url = ('/show_some')


class GeeksList(ListView):
    # specify the model for list view
    model = GeeksModel
    raise_exceptionq = False
    login_url = '/register/'


class GeeksDetailView(DetailView):
    model = GeeksModel


class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = [
        "title",
        "description"
    ]
    success_url = ('/show_some')


class GeeksDeleteView(DeleteView):
    model = GeeksModel
    success_url = "/show_some"
