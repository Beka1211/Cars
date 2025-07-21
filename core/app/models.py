from django.db import models
class Category(models.Model):
    title=models.CharField(max_length=222)

    def __str__(self):
        return self.title

class Auto_show(models.Model):
    title=models.CharField(222)
    model_car=models.CharField(222)
    number=models.CharField(max_length=8)
    price=models.DecimalField(decimal_places=2,max_digits=12)
    year=models.PositiveSmallIntegerField()
    image=models.ImageField(upload_to='media/car_image')
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
