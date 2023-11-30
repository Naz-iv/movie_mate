from django.urls import path

from movies.views import MovieListView

urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    path('movies/', MovieListView.as_view(), name='movie_list')
]

app_name = "movies"
