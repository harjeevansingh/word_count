from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.homepage, name='home'),
	path('count/', views.count, name='count'),
	path('about/', views.about, name='about'),

]
