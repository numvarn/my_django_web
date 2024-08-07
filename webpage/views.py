from django.shortcuts import render

# Create your views here.


def indexPage(request):
    return render(request, "index.html")


def aboutPage(request):
    return render(request, "about.html")


def forPage(request):
    return render(request, 'for_test.html')
