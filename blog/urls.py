from django.urls import path
from .views import GeeksCreate, GeeksList, GeeksDetailView, GeeksUpdateView, GeeksDeleteView

app_name = 'blog'
urlpatterns = [
    path('show_some/create_some/', GeeksCreate.as_view(), name='create_some'),
    path('show_some/', GeeksList.as_view()),
    path('show_some/<int:pk>/', GeeksDetailView.as_view()),
    path('show_some/<int:pk>/update', GeeksUpdateView.as_view()),
    path('show_some/<int:pk>/delete/', GeeksDeleteView.as_view()),
]
