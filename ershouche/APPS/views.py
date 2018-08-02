from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')


def error(request):

    return render(request, '404.html')


def about(request):

    return render(request, 'about.html')


def car_info(request):

    return render(request, 'car_info.html')


def buy_car(request):

    return render(request, 'buy_car.html')
