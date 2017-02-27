#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from AddressBookApp.models import *
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import logging

# Create your views here.

logger = logging.getLogger('AddressBookLog')

def getlist(request):
    information = Information.objects.all()
    return render(request, 'contactsList.html', {'informtion':information})

@login_required()
def addlist(request):
    if request.method == 'GET':
        return render(request, 'addContacts.html')
    elif request.method == 'POST':
        post = request.POST
        new_contack = Information(
            name=post["name"],
            phone=post["phone"],
            email=post["email"],
            address=post["address"],
            qq=post["qq"],)
        new_contack.save()
        information = Information.objects.all()
        return render(request, 'contactsList.html', {'informtion': information})

@login_required()
def updatelist(request):
    if request.method == 'GET':
        contackid = request.GET['contackid']
        contack = Information.objects.get(id=contackid)
        return render(request, 'updateContacks.html', {'contack':contack})
    elif request.method == 'POST':
        contackid = request.POST['id']
        old_contack = Information.objects.get(id=contackid)
        old_contack.name = request.POST["name"]
        old_contack.phone = request.POST["phone"]
        old_contack.email = request.POST["email"]
        old_contack.address = request.POST["address"]
        old_contack.qq = request.POST["qq"]
        old_contack.save()
        information = Information.objects.all()
        return render(request, 'contactsList.html', {'informtion': information})

@login_required()
def dellist(request):
    contackid = request.GET['contackid']
    Information.objects.get(id=contackid).delete()
    information = Information.objects.all()
    return render(request, 'contactsList.html', {'informtion': information})


def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                #重定向到成功页面
            else:
                #提示错误信息
                warning1 = "登陆失败！"
                return render(request, 'login.html', {'warning': warning1})
        else:
            #提示错误信息
            warning2 = "用户不存在或密码错误！"
            return render(request, 'login.html', {'warning': warning2})
        return HttpResponseRedirect("/")

def my_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



