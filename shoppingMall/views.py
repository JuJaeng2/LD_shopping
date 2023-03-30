# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# def index(request):
#     Users = User.objects.all()

#     return render(request, 'test_connection.html',{
#         "users" : Users,
#         })

def mainPage(request):
    
    image = Cloth.objects.all()
    outer_data = []
    top_data = []
    bottom_data = []
    all =[]
    # 카테고리 별로 분류 -> 구매 개수, 이미지 링크 짝지어서 리스트에 넣기
    for i in image:
        if i.c_category == 'outer':
            outer_data.append([i.c_countBuy, i.c_image])
        elif i.c_category == 'bottom':
            bottom_data.append([i.c_countBuy, i.c_image])
        else:
            top_data.append([i.c_countBuy, i.c_image])
    
    all += [outer_data] + [top_data] + [bottom_data]
    result = []
    
    # 구매개수 기준 정렬
    for l in all:
        l.sort(key = lambda x: x[0], reverse=True)
        result.append([l[0:3]])
    
    outer = result[0]
    top = result[1]
    bottom = result[2]
            
    context = {
        'outer' : outer,
        'top' : top,
        'bottom' : bottom
    }
    return render(request, 'project.html', context)








# <<<@@ TEST @@>>>

def upload_imgae(request):

    if request.method == 'POST':
        test = Test()

        test.imagePath = request.FILES['imgfile']
        test.save()

    image = Test.objects.all()

    return render(request, 'result.html', context={
        'image' : image
    })

def home(request):
    return render(request, 'test_connection.html')

def check(request):

    test = Test.objects.all()
    

    return render(request, 'result.html', context={
        'image' : test
    })