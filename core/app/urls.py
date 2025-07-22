from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index_views,name='index'),
    path('car/<int:car_id>/', views.car_detail_view, name='car_detail'),
    path('car_create/',views.car_create_view, name='car_create'),
    path('car/<int:pk>/edit/', views.car_update, name='car_update'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('user_register/', views.user_register_view, name='register'),
    path('user_login/', views.user_login_view, name='login'),
    path('user_logout/', views.user_logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)