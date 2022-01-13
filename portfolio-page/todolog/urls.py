from django.urls import path
from todolog import views
from . import views

app_name = 'todolog'

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('current/', views.currenttodos, name='currenttodos'),
]
