from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto_show, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def index_views(request):
    cars=Auto_show.objects.all()
    return render(request,'app/car_views.html',{'cars':cars})

def car_detail_view(request, car_id):
    car = Auto_show.objects.filter(id=car_id).first()
    return render(request, 'app/detail.html', {'car': car})

def car_create_view(request):
    if not request.user.is_authenticated:
        return redirect('index')

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
            user=request.user,
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

def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно содали аккаунт')
            return redirect('index')

        for field, errors in form.errors.items():

            for error in errors:
                messages.error(request, f'{error}')

    form = UserCreationForm()

    return render(request=request, template_name='app/user_register.html', context={"form": form})


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('index')

        messages.error(request, 'Неправильный логин или пароль')

    return render(request, 'app/user_login.html')


def user_logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('index')