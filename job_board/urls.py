from django.urls import path
from job_board.views import *

urlpatterns = [
    path('', index),
    path('job/<int:pk>/', job_detail, name='job-detail')
]