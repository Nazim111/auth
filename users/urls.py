from django.urls import path, include

# from users.views import Register
from users import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),

    # path('register/', Register.as_view(), name='register'),
]
