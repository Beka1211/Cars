from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto_show, Category

def index_views(request):
    cars=Auto_show.objects.all()

    return render(request,'app/car_views.html',{'cars':cars})

def car_detail_view(request, car_id):
    car = Auto_show.objects.filter(id=car_id).first()
    return render(request, 'app/detail.html', {'car': car})

def car_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category_id')
        model_car = request.POST.get('model')
        number = request.POST.get('number')
        year = request.POST.get('year')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id)

        Auto_show.objects.create(
            title=title,
            category_id=category,
            model_car=model_car,
            number=number,
            year=year,
            price=price,
            image=image
        )

        return redirect('index')

    categories = Category.objects.all()
    return render(request, 'app/user.html', {'categories': categories})

def car_update(request, pk):
    car = get_object_or_404(Auto_show, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        car.title = request.POST.get('title')
        car.model_car = request.POST.get('model')
        car.number = request.POST.get('number')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')

        category_id = request.POST.get('category_id')
        car.category_id = Category.objects.get(id=category_id)

        if request.FILES.get('image'):
            car.image = request.FILES['image']

        car.save()
        return redirect('car_detail', car.id)

    return render(request, 'app/car_update.html', {'car': car, 'categories': categories})

def car_delete(request, pk):
    auto_shows = get_object_or_404(Auto_show, pk=pk)
    auto_shows.delete()

    return redirect('index')