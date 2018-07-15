from django.contrib import admin
from django.urls import path,re_path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^time/plus/(\d{1,2})/$',views.current_datetime),
    path('hello/',views.hello),
    path('',views.index),
]
