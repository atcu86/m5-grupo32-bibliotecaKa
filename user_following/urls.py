from django.urls import path
from . import views

urlpatterns = [
    path("users/following/<pk:book_id>", views.UserDetailView.as_view()),
]
