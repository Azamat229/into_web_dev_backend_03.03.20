
from django.contrib import admin
from django.urls import path, include

# from register import  register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),
    path('register/', include('register.urls')),
    # path('login/', include('login.urls'))

]

