from django.shortcuts import render

# Create your views here.


def indexPage(request):
    return render(request, "index.html")


def aboutPage(request):
    return render(request, "about.html")


def forPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'for_test.html', context)


def cardColorPage(request):
    context = {
        'color': 'all',
    }

    if request.method == "GET" and request.GET.get('color') != None:
        context['color'] = request.GET.get('color')

    return render(request, 'card_color.html', context)
