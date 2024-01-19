from django.shortcuts import render, redirect
from .forms import CatagoryForm

# Create your views here.
def create_catagory(request):
    form = CatagoryForm()
    
    if request.method == 'POST':
        form = CatagoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect("create_catagory")
    
    return render(request, './catagory/CreateCatagory.html', {"form": form})