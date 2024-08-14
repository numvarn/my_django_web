from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name="index"),
    path("about/", views.aboutPage, name="about"),
    path("for/", views.forPage, name='for-page'),
    path("color/", views.cardColorPage, name='color-page'),
    path("form/", views.formPage, name='form-page'),
]
