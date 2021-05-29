from django.contrib import admin
from django.urls import path

from machinelearning import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # add these to configure our home page (default view) and result web page
    path('', views.home, name='index'),
    path('result/', views.result, name='result'),
]
