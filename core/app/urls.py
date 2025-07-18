from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index_views,name='index'),
    path('car/<int:car_id>/', views.car_detail_view, name='car_detail'),
    path('car_create/',views.car_create_view, name='car_create')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)