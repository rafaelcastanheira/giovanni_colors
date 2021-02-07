from django.urls import path

from . import views

urlpatterns = [
    # path('', views.portfolio, name="portfolio"),
    path('<str:art_type>/', views.portfolio, name="portfolio"),
]
