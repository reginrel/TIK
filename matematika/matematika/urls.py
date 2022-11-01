from django.contrib import admin
from django.urls import path
from doss.views import doss
from matkul.views import matkul
from sejar.views import sejar
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doss/', doss),
    path('matkul/', matkul),
    path('sejar/', sejar),
    path('', views.index),
]
