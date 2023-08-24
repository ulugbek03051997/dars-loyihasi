from django.urls import path
from .views import HomePageView,AboutPageView,Baholar


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('baho/',Baholar.as_view(),name='baho'),
]