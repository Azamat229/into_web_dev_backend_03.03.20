
from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register')
    # path('update/', ProfileUpdateView.as_view(), name='profile-update'),

]
