from django.urls import path
from . import views

app_name = 'program-management'

urlpatterns = [
    path('', views.showProgramManagementDashboard, name='programManagementDashboard'),
]
