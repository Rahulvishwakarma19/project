from django.urls import path
from notice_board import views

urlpatterns = [
    path('',views.notice,name="notice"),
]