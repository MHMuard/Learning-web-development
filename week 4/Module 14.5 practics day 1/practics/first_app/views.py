from django.shortcuts import render
from .forms import contactForm, GeeksForm, ExampleForm, StudentData, PasswordValidationProject

# Create your views here.

def home(request):
    return render(request, './first_app/home.html')

def ordinarycoders(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = ExampleForm()  # Fix indentation here
    return render(request, './first_app/ordinarycoders.html', {'form': form})

def geeksforgeeks(request):
    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = GeeksForm()  # Fix indentation here
    return render(request, './first_app/geeksforgeeks.html', {'form1': form})
