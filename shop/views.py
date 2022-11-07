from django.shortcuts import render
from shop.models import Shop
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage

import datetime
import random
import sys, os

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# def index(request):
#     return HttpResponse('''
#     <html>
#         <body>
#         <h1> 안녕하세요 ! </h1>
#         </body>
#     </html>
#     ''')

def index(request):
    print("index")
    rsshop = Shop.objects.all()

    return render(request, "index.html", {
        'rsshop': rsshop
    })

# 어떤 데이터를 넘겨줄지 ? => rsshop

def about(request):
    print("about")
    return render(request, "about.html")

def services(request):
    print("services")
    return render(request, "services.html")

def contact(request):
    print("contact")
    return render(request, "contact.html")

def works(request): # 메인 페이지랑 유사하다.
    print("works")
    rsshop = Shop.objects.all()

    return render(request, "works.html", {
        'rsshop': rsshop
    })



def workSingle(request, no):
    print("workSigle")
    shop = Shop.objects.get(no=no)
    return render(request, "work-single.html", {
        'shop': shop
    })


def workReg(request):
    print("workReg")
    return render(request, "work-reg.html")


def workPro(request):
    no = request.POST['no']
    title = request.POST['title']
    category = request.POST['category']
    summary = request.POST['summary']
    subject = request.POST['subject']
    contents = request.POST['contents']

    dt_now = datetime.datetime.now()
    str_date = dt_now.strftime('%Y_%m_%d_%H%M_%f')
    if 'ufile' in request.FILES:
        uploaded_file = request.FILES['ufile']
        org_file_name = uploaded_file.name
        print('{}'.format(org_file_name))
        name_ext = os.path.splitext(org_file_name)[1]
        new_file_name = 'shop' + str_date + '_' + str(random.randint(1000000000, 9999999999))
        new_file_location = 'shop/static/upload/photos'
        fs = FileSystemStorage(location=new_file_location) # 객체 만들어주기

        name = fs.save(new_file_name + name_ext, uploaded_file)

    if no in (None, ''): # 메소드(걍 함수라고 생각해)
        rows = Shop.objects.create(
            title=title,
            category=category,
            summary=summary,
            subject=subject,
            contents=contents,
            org_file_name=org_file_name,
            file_name=name,
            file_location=new_file_location # 얘네는 클래스에 매개변수로
        )
    else:
        shop = Shop.objects.get(no=no)
        shop.title = title
        shop.category = category
        shop.summary = summary
        shop.subject = subject
        shop.contents = contents
        if 'ufile' in request.FILES:
            shop.org_file_name = org_file_name
            shop.file_name = name
            shop.file_location = new_file_location # 얘네는 클래스에 값 넣기
        shop.save()
    return redirect('/works')

def workModify(request, no):
    print("workModify")
    shop = Shop.objects.get(no=no)
    return render(request, "work-reg.html", {
        'shop': shop
    })

def workRemove(request, no):
    Shop.objects.filter(no=no).delete()
    return redirect('/works')