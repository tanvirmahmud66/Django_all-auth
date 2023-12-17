from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'app/index.html')

def DashBoard(request):
    return render(request, 'app/dashboard.html')