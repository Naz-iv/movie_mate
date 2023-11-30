from django.urls import path

from movies.views import MovieList

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie_list')
]

app_name = "movies"
