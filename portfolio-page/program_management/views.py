from django.shortcuts import render

# Create your views here.

def showProgramManagementDashboard(request):
    return render(request, 'program_dashboard.html')
