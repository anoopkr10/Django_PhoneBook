from django.contrib import admin
from django.urls import path

from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.insert),
    path('home/',views.insert,name='home'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
]
