from django.urls import path
from job_board.views import *

urlpatterns = [
    path('', index),
]