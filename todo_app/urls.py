# from django.urls import path
# from .views import create_movie, get_movie, create_rating

# urlpatterns = [
#     path('movies/', create_movie),
#     path('movies/<int:id>/', get_movie),
#     path('ratings/', create_rating),
# ]

from django.urls import path
from .views import CreateMovieView, GetMovieView, CreateRatingView

urlpatterns = [
    
    path('movies/', CreateMovieView.as_view()),
    path('movies/<int:id>/', GetMovieView.as_view()),
    path('ratings/', CreateRatingView.as_view()),
]
