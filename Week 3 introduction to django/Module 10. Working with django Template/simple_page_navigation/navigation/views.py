from django.shortcuts import render

# Create your views here.
def content(request):
    return render(request,'navigation/content.html')

def about(request):
    return render(request,'navigation/about.html')
