from django.contrib import admin
from django.urls import path

from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/expenses/', views.expenses_api, name='expenses_api'),
    path('', views.dashboard, name='dashboard'),
]
