from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Kouka2
from .forms import Kouka2Form, FindKouka2

def index(request):
    params = {
        'title':'農産物商品',
        'data':Kouka2.objects.all(),
    }

    return render(request, 'kouka2/index.html', params)

def create(request):
    if request.method == 'POST':
        obj = Kouka2()
        kouka2 = Kouka2Form(request.POST, instance=obj)
        kouka2.save()
        return redirect(to='/kouka2')
    params = {
        'title':'農産物商品',
        'form':Kouka2Form()
    }
    return render(request, 'kouka2/create.html', params)

def edit(request, num):
    obj = Kouka2.objects.get(id=num)
    if (request.method == 'POST'):
        kouka2 = Kouka2Form(request.POST, instance=obj)
        kouka2.save()
        return redirect(to='/kouka2')
    params = {
        'title':'農産物商品',
        'id':num,
        'form': Kouka2Form(instance=obj),
    }
    return render(request, 'kouka2/edit.html', params)

def delete(request, num):
    kouka2 = Kouka2.objects.get(id=num)
    if (request.method == 'POST'):
        kouka2.delete()
        return redirect(to='/kouka2')
    params = {
        'title': '農産物商品',
        'id':num,
        'obj': kouka2,
    }
    return render(request, 'kouka2/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        form = FindKouka2(request.POST)
        find = request.POST['find']
        val = find.split()
        data = Kouka2.objects\
            .filter(price__gte=val[0])\
            .filter(price__lte=val[1])
    else:
        form = FindKouka2()
        data = Kouka2.objects.all()
    params = {
        'title': '農産物商品',
        'form':form,
        'data':data,
    }
    return render(request, 'kouka2/find.html', params)