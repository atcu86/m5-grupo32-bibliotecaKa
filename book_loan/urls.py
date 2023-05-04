from django.urls import path
from . import views

urlpatterns = [
    path("bookloan/<uuid:bookloan_id>/", views.BookLoanView.as_view()),
    path(
        "bookloan/<uuid:bookloan_id>/devolution/",
        views.BookLoanDetailView.as_view(),
    ),
]
