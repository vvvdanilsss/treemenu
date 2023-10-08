from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# def about(request):
#     return render(request, 'about.html')


def team(request):
    return render(request, 'team.html')


def history(request):
    return render(request, 'history.html')


def mission(request):
    return render(request, 'mission.html')


def contact(request):
    return render(request, 'contact.html')


def support(request):
    return render(request, 'support.html')
