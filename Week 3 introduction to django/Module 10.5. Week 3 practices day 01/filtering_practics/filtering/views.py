from django.shortcuts import render

# Create your views here.
def geeksforgeeks(request):
    data = {
        'list': ['a', 'b', 'c', 'd'],
        'val': 4, 
        'addslash':"I'm Jai",
        'cap': 'jai',
        'c': 'String with spaces',
        'd': '',
        'di': [
                {'name': 'zed', 'age': 19},
                {'name': 'amy', 'age': 22},
                {'name': 'joe', 'age': 31},
            ],
        'l' : "Murad",
        's': 'Jai is a slug'
        }
    return render(request, "filtering/geeks.html", data)

def earthly(request):
    return render(request, "filtering/earthly.html")