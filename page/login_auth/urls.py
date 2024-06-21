from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.recommend_movies, name='recommend_movies'),
    path('signup/', views.authView, name='signup'),  # URL for signup (custom view)
    path('logout/', views.custom_logout, name='logout'),  # URL for logout (custom view)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
     path('movie_info/<str:title>/', views.movie_info, name='movie_info'),# URL for login (Django's LoginView)
]
