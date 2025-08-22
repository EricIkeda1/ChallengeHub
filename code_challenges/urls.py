from django.contrib import admin
from django.urls import path
from challenges import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('challenges/', views.challenges_list, name='challenges_list'), 
    path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'), 
]
