from django.shortcuts import render

# Create your views here.


def member_center(request):
    if request.method == 'GET':
        return render(request,'会员中心.html')

def index(request):
    return render(request,'index.html')


def my_request(request):
    return render(request,'会员中心_我的需求.html')

def account_manager(request):
    return render(request,'会员中心_账户管理.html')

def list(request):
    return render(request,'list.html')

def wymc(request):
    return render(request,'wymc.html')