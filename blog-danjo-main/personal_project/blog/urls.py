from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),  # Shows all blogs
    path('<int:blog_id>', views.details, name='details'),  # Shows a specific blog by ID
    path('all_blogs/', views.all_blogs, name='all_blogs'),
]
