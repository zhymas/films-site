from django.shortcuts import render


def home(request):
    print(request.user)
    return render(request, 'films/base.html')
