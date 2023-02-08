from django.urls import path
from .views import register

from . import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('whoami', views.whoami),
    path('register/', views.register)
    # path('danielzin',views.danielzin)
]
