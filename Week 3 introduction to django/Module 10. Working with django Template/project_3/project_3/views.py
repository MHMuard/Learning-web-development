from django.shortcuts import render

def home(request):
    d = {'author': 'Rahim', 'age': 20, 'course':[
        {"id": 1,
         'name': 'python',
         'fee': 5000,
        },
        {"id": 2,
         'name': 'django',
         'fee': 10000,
        },
        {"id": 3,
         'name': 'c',
         'fee': 1000,
        }
    ] }

    return render(request, 'home.html', d)
