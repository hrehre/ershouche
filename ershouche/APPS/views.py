import re

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from APPS.models import User
from utils import codes


def index(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request, 'index.html')


def error(request):
    """
    错误页面
    :param request:
    :return:
    """
    return render(request, '404.html')


def about(request):
    """
    关于页面
    :param request:
    :return:
    """
    return render(request, 'about.html')


def car_info(request):
    """
    汽车详情页面
    :param request:
    :return:
    """
    return render(request, 'car_info.html')


def buy_car(request):
    """
    我要买车
    :param request:
    :return:
    """
    return render(request, 'buy_car.html')


def register(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if not all([mobile, name, password]):
            return JsonResponse(codes.REGISTER_NOT_ALL)
        if not re.match(r'^1[34578]\d{9}$', mobile):
            return JsonResponse(codes.REGISTER_MOBILE_NOT_VALID)
        user = User.objects.filter(phone_num=mobile).first()
        if user:
            return JsonResponse(codes.MOBILE_IS_REGISTED)
        else:
            password_hash = make_password(password)
            User.objects.create(username=name, phone_num=mobile, password=password_hash)
            return JsonResponse(codes.SUCCESS)


def login(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        user = User.objects.filter(phone_num=mobile).first()
        if not user:
            return JsonResponse(codes.MOBILE_OR_PASSWORD_ERROR)
        if user:
            password_hash = user.password
            if not check_password(password, password_hash):
                return JsonResponse(codes.MOBILE_OR_PASSWORD_ERROR)
            else:
                pass