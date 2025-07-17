from django.shortcuts import render
from .models import Auto_show

def index_views(request):
    cars=Auto_show.objects.all()

    return render(request,'app/car_views.html',{'cars':cars})

def car_detail_view(request, car_id):
    car = Auto_show.objects.filter(id=car_id).first()
    return render(request, 'app/detail.html', {'car': car})