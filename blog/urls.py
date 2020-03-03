# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('blog', views.index, name='index')
# ]

from django.urls import path
from .views import InfoList, GeeksCreate, GeeksList, GeeksDetailView, GeeksUpdateView, GeeksDeleteView

from . import views

app_name = 'blog'
urlpatterns = [
    path('', InfoList.as_view()),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('show_some/create_some/', GeeksCreate.as_view(), name='create_some'),
    path('show_some/', GeeksList.as_view()),
    path('show_some/<pk>/', GeeksDetailView.as_view()),
    path('show_some/<pk>/update', GeeksUpdateView.as_view()),
    path('show_some/<pk>/delete/', GeeksDeleteView.as_view()),

    # path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),

    # path('update/', ProfileUpdateView.as_view(), name='profile-update'),
]
