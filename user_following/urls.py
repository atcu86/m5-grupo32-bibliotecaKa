from django.urls import path
from . import views

urlpatterns = [
    path("users/following/<uuid:book_id>/", views.UserFollowingView.as_view()),
    path("users/following/book/<uuid:book_id>/", views.BookFollowersView.as_view()),
]
