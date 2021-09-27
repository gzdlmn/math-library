from django.contrib import admin
from django.urls import path
from . import views
app_name="library"
urlpatterns=[
    path("fouroperations", views.four_operations, name="fouroperations"),
    path("trigonometry", views.trigonometry_operations, name="trigonometry"),
    path("functions", views.all_functions, name="functions"),
    path("geometry", views.geometry, name="geometry"),
]