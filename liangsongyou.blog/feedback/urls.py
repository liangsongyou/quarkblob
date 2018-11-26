from django.urls import path
from feedback import views

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('<slug:slug>/',views.feedback_item, name='feedback_item'),
]