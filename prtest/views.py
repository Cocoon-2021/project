from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Details
from django.http import HttpResponse
from django.contrib import messages
import re


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        num = request.POST['num']
        dob = request.POST['dob']
        pname = request.POST['pname']
        pnum = request.POST['pnum']
        passwd = request.POST['passwd']
        passwd1 = request.POST['passwd1']
        lst = []
        obj = Details()
        obj.name = name
        obj.dob = dob
        obj.pname = pname
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        preg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        # if re.fullmatch(regex, email):
        #     obj.email = email
        #     if len(num) == 10:
        #         obj.num = num
        #         if len(pnum) == 10:
        #             obj.pnum = pnum
        #             if passwd == passwd1:
        #                 pat = re.compile(preg)
        #                 mat = re.search(pat, passwd)
        #                 if mat:
        #                     obj.passwd = passwd
        #                 else:
        #                     lst.append("Password invalid !!")
        #
        #             else:
        #                 lst.append("passwords are mismatched")
        #
        #         else:
        #             lst.append("parent number doesn't follow property")
        #
        #     else:
        #         lst.append("number doesn't follow property")
        #
        # else:
        #     lst.append("email validation error")
        if re.fullmatch(regex, email):
            obj.email = email
        else:
            lst.append("email validation error")
        if len(num) == 10:
            obj.num = num
        else:
            lst.append("number doesn't follow property")
        if len(pnum) == 10:
            obj.pnum = pnum
        else:
            lst.append("parent number doesn't follow property")
        if passwd == passwd1:
            pat = re.compile(preg)
            mat = re.search(pat, passwd)
            if mat:
                obj.passwd = passwd
            else:
                lst.append("Password invalid !!")
        else:
            lst.append("passwords are mismatched")

        if len(lst) > 0:
            print(lst)
            messages.error(request, lst)
            return render(request, 'index.html')
        print(name, email, gender, num, dob, pname, pnum, passwd)
        obj.save()

    return render(request, 'index.html')


def detail(request):
    lst2=[]
    if request.method == 'POST':
        email = request.POST['email']
        passwd = request.POST['passwd']
        check = Details.objects.all().filter(email=email, passwd=passwd)
        print(check)
        if check:
            print("login sucessfull")
            print(Details.email, Details.name)
            return render(request, 'details.html', {'display': check})
        else:
            messages.success(request, "Invalid Credentials")
            return render(request, 'details.html', {'display': check})
    return render(request, 'details.html')
# Create your views here.
