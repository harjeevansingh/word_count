from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.homepage, name='home'),			# Home Page
	path('count/', views.count, name='count'),   # Count page
	path('about/', views.about, name='about'),		# About Page

]
