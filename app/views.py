from django.shortcuts import render

# Create your views here.
def royal(request):
    return render(request,'royal.html',context={'name':'potti'})