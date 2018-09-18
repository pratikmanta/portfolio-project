from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('<int:job_id>/', views.job_details,name="job_details")
    ]
