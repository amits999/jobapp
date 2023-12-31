from django.urls import path
from app import views

urlpatterns = [
    path('hello', views.hello, name='hello_page'),
    path('', views.display_jobs, name='main_page'),
    path('job/<int:id>', views.job_detail_page, name='jobs_detail'),
]