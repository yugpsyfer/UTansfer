from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('make_user/', views.make_user, name='make_user'),
    path('upload/', views.upload, name='upload'),
    path('showfiles/', views.showfiles, name='showfiles'),
]
